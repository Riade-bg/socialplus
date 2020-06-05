from .models import Notifications
from django.dispatch import receiver
from django.db.models.signals import m2m_changed, post_save
from django.core.signals import request_finished
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync
from django.contrib.humanize.templatetags import humanize


@receiver(post_save, sender=Notifications)
def new_like(sender, instance, created, **kwargs):
        if created:
            obj = sender.objects.get(id=instance.id)
            if str(obj.user_who_like) != str(obj.post_username):
                channel_layer = get_channel_layer()
                humanize.naturaltime(obj.date)
                async_to_sync(channel_layer.group_send)(
                    "notify_user"+str(obj.post_username), {
                        "type": "user.gossip",
                        "event": "New Like",
                        "username_who_like": str(obj.user_who_like),
                        "post_username": str(obj.post_username),
                        "post_id" : str(obj.post.id),
                        "html":"<div class='notification-container' href='"+str(obj.user_who_like)+"'>\
                                    <img src='"+str(obj.user_who_like.profile.avatar.url)+"' class='float-left'>\
                                    <span class='mr-1'>"+str(obj.user_who_like)+"</span>\
                                    Had Liked Your post\
                                    <p class='mt-1'><i class='fas fa-clock mr-1'></i>"+ str(humanize.naturaltime(obj.date)) +"</p>\
                                </div>"
                    }
                )