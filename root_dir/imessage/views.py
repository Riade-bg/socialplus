from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile
from .models import imessage
from django.db.models import Q
from .forms import MessageVerfication
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models import Count


def messanger_home(request):
    form = MessageVerfication()
    users = Profile.objects.exclude(user__username = request.user)
    messages = imessage.objects.filter(sender = request.user)

    duplicates_messages = imessage.objects.filter(sender__username = request.user).values('reciever_id', "message").order_by('-date').distinct()
    result = []
    seen = []
    for data in range(len(duplicates_messages)):
        if duplicates_messages[data]['reciever_id'] not in seen:
            seen.append(duplicates_messages[data]['reciever_id'])
            result.append(duplicates_messages[data])
        
    contex = {
        "users_data":users,
        "form":form,
        "last_messages":result,
    }
    return render(request, 'imessage/home.html', contex)

def messanger_create(request):
    reciever = request.POST.get("reciever", None)
    message = request.POST.get("message", None)
    user = User.objects.get(id = reciever)
    html = []
    form = MessageVerfication(request.POST)
    if form.is_valid():    
        obj = imessage.objects.create(
            sender = request.user,
            reciever = user,
            message = message,
            date = timezone.now()
        )
        event_triger(reciever, message, request.user.id)
        msg = imessage.objects.values().filter(reciever__id = reciever, sender__username = request.user).order_by('-date')[:1]
        html.append("<div class='container-message d-flex justify-content-end float-right'>\
                        <p class='text-right mr-3 align-self-center'>"+ msg[0]['message'] +"</p>\
                    </div>")
        return HttpResponse(html)
    else:
        errors = {
            "status": 505,
            "Error": "Message Is Require"
        }
        return JsonResponse(errors)

def messanger_show(request):
    reciever_ = request.POST.get("reciever", None)
    user = request.POST.get("user", None)
    html = []
    if int(user) == int(request.user.id):
        messages = imessage.objects.values().filter(Q(reciever__id = reciever_, sender__id = user) | Q(reciever__id = user, sender__id = reciever_)).order_by('date')
        for mesg in range(len(messages)):
            if int(messages[mesg]['sender_id']) == int(request.user.id):
                html.append("<div class='container-message d-flex justify-content-end float-right'>\
                                <p class='text-right mr-3 align-self-center'>"+ messages[mesg]['message'] +"</p>\
                            </div>")
            else:
                html.append("<div class='container-message float-left'>\
                                <p class='text-left reciever ml-3'>"+ messages[mesg]['message'] +"</p>\
                            </div>")
    else:
        html = "ERROR"
    return JsonResponse({
        "html":html,
        "user":str(reciever_)
    })




def event_triger(user, message, loged_in_user):
    send_msg = "<div class='container-message float-left'><p class='text-left reciever ml-3'>"+ message +"</p></div>"
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        str(user)+'_room',
        {
            'type': 'send_message_to_frontend',
            'message': send_msg,
            'id':str(loged_in_user)
        }
    )
