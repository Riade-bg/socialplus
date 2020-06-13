from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm, ProfilePictureUpdate
from django.contrib import messages
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from .models import PostCreate, Bookmark, Notifications
from users.models import Profile
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

@login_required
def home(request):
    post = PostCreate.objects.all().order_by('-date')
    notifications = Notifications.objects.filter(post_username = request.user).order_by('-date')
    contex={
        'Posts':post,
        'notifications':notifications
    }
    return render(request, 'social/home.html', contex)


@login_required
def create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user_name = request.user
            form.save()
            return redirect('/')
    else:
        form = PostCreateForm()
    contex = {
        'form':form
    }
    return render(request, 'social/create.html', contex)




def delete(request, id):
    obj = PostCreate.objects.get(id=id)
    if obj.user_name == request.user:
        obj.delete()
    return redirect('/')




def Like(request):
    id_ = request.POST.get("id")
    user_ = request.user
    obj = get_object_or_404(PostCreate, id=id_)
    notification = Notifications.objects.all()
    post_user = obj.user_name
    if user_.is_authenticated:
        if user_ in obj.likes.all():
            obj.likes.remove(user_)
            if notification.exists():
                n = Notifications.objects.get(post = obj)
                n.delete()
        else:
            obj.likes.add(user_)
            if str(user_) != str(post_user):
                Notifications.objects.create(
                    user_who_like = user_,
                    post = obj,
                    post_username = post_user
                )
    obj_ = obj.likes.count()
    return HttpResponse(obj_)




@login_required
def bookmark(request):
    bk = Bookmark.objects.filter(user__username = request.user)
    if bk.count() > 0:
        contex = {
            'bookmarks':bk
        }
    else:
        contex = {
            'bk':"No Bookmarks To Show"
        }
    return render(request, 'social/bookmarks.html', contex)


def create_bookmark(request):
    id_ = request.POST.get("id", None)
    post = PostCreate.objects.get(id=id_)
    bk = Bookmark.objects.all()
    user = post.user_name
    delete = False
    created = False
    if bk.exists():
        bookmarks = Bookmark.objects.filter(bookmark__id = post.id)
        if bookmarks.count() > 0:
            bookmarks.delete()
            delete = True
            created = False
        else:
            Bookmark.objects.create(
                user = request.user,
                bookmark = post
            )
            created = True
    else:
        Bookmark.objects.create(
            user = request.user,
            bookmark = post
        )
        created = True

    if created:
        html = "<div class='alert alert-success alert-dismissible fade show' role='alert'>\
        <b>" + str(user) +" Post</b> Was Successfully Saved.\
        <button type='button' class='close' data-dismiss='alert' aria-label='Close'>\
        <span aria-hidden='true'>&times;</span></button></div>"
    elif delete:
        html = "<div class='alert alert-success alert-dismissible fade show' role='alert'>\
        <b>" + str(user) +" Post</b> Was Removed From Bookmarks.\
        <button type='button' class='close' data-dismiss='alert' aria-label='Close'>\
        <span aria-hidden='true'>&times;</span></button></div>"
    else:
        html = "<div class='alert alert-danger alert-dismissible fade show' role='alert'>\
         There Was An Error, Please Try Again.\
        <button type='button' class='close' data-dismiss='alert' aria-label='Close'>\
        <span aria-hidden='true'>&times;</span></button></div>"
    return HttpResponse(html)


@login_required
def profile(request, slug):
    posts = PostCreate.objects.filter(user_name__username__exact = slug).order_by('-date')
    user_ =  Profile.objects.get(user__username = slug)
    p_form = ProfilePictureUpdate()
    contex = {
        'Posts':posts,
        'user_':user_,
        'form':p_form
    }
    return render(request, 'social/profile.html', contex)

def profileChange(request):
    if request.method == "POST":
        p_form = ProfilePictureUpdate(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('/')
        else:
            return redirect('/')
    return redirect('/')

@login_required
def SearchAPI(request):
    search_data = request.POST.get('search_term', None)
    users =  Profile.objects.filter(user__username__contains = search_data)
    html = []
    for u in users:
        html.append(
            '<a class="card-body container-search" href="../profile/' 
            +str(u.user)+ '"><img src='+u.avatar.url+
            ' class="d-inline mr-1"><h6 class="text-left d-inline">'
            +str(u.user)+'</h6></a>')
    return HttpResponse(html)




def show_post(request, pk):
    post = PostCreate.objects.get(id = pk)
    notification = Notifications.objects.get(post__id = pk)
    notification.delete()
    contex = {
        'post':post
    }
    return render(request, 'social/show_post.html', contex)
