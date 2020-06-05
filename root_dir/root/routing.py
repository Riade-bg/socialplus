from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from channels.sessions import SessionMiddlewareStack

from social.consumer import NoseyConsumer
from imessage.consumer import ChatConsumer
application = ProtocolTypeRouter({
    'websocket': SessionMiddlewareStack(
        AuthMiddlewareStack(URLRouter(
                [
                    path('notify/', NoseyConsumer),
                    path('chat/', ChatConsumer),
                ]
       ))
    )
})
            

