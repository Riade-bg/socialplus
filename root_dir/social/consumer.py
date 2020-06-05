import json
import asyncio
from channels.generic.websocket import (AsyncJsonWebsocketConsumer,
                                        WebsocketConsumer)
from .models import PostCreate


class NoseyConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.user = self.scope["user"]
        self.user_room_name = "notify_user"+str(self.user.username)
        await self.channel_layer.group_add(
            self.user_room_name,
            self.channel_name
        )



    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("gossip", self.channel_name)

    async def user_gossip(self, event):
        await self.send_json(event)
