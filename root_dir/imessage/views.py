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



def messanger_home(request):
    users = Profile.objects.exclude(user__username = request.user)
    messages = imessage.objects.filter(sender = request.user)
    # last_messages = imessage.objects.values().filter(sender = request.user).order_by('-date')
    # reciever = User.objects.get(id = last_messages[0]['reciever_id'])

    form = MessageVerfication()
    contex = {
        "users_data":users,
        "form":form
    }
    return render(request, 'imessage/home.html', contex)

def messanger_create(request):
    reciever = request.POST.get("reciever", None)
    message = request.POST.get("message", None)
    user = User.objects.get(username = reciever)
    html = []
    form = MessageVerfication(request.POST)
    if form.is_valid():    
        obj = imessage.objects.create(
            sender = request.user,
            reciever = user,
            message = message,
            date = timezone.now()
        )
        event_triger(reciever, message)
        msg = imessage.objects.values().filter(reciever__username = reciever, sender__username = request.user).order_by('-date')[:1]
        html.append("<div class='msg-container-sender mb-2'>\
                                <p class='text-left'>" + msg[0]['message'] + "</p>\
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
    if str(user) == str(request.user):
        messages = imessage.objects.values().filter(Q(reciever__username = reciever_, sender__username = user) | Q(reciever__username = user, sender__username = reciever_)).order_by('date')
        for mesg in range(len(messages)):
            if int(messages[mesg]['sender_id']) == int(request.user.id):
                html.append("<div class='msg-container-sender mb-2'>\
                            <p class='text-left'>" + messages[mesg]['message'] + "</p>\
                            </div>")
            else:
                html.append("<div class='msg-container-reciever mb-2'>\
                            <p class='text-left'>" + messages[mesg]['message'] + "</p>\
                            </div>")
    else:
        html = "ERROR"
    return HttpResponse(html)




def event_triger(user, message):
    send_msg = "<div class='msg-container-reciever mb-2'><p class='text-left'>" + message + "</p></div>"
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        str(user)+'_room',
        {
            'type': 'send_message_to_frontend',
            'message': send_msg
        }
    )
