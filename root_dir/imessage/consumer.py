import json
import asyncio
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from channels.generic.websocket import WebsocketConsumer
from django.http import HttpResponse

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['user'].id
        self.room_group_name = str(self.room_name)+"_room"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print("DISCONNECED CODE: ",code)

  
    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        user = data['id']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                "type": 'send_message_to_frontend',
                "message": message,
                "id":user
            }
        )


    def send_message_to_frontend(self,event):
        message = event['message']
        user = event['id']
        data = {"message":"//"+str(message)+"//", "user":"//"+str(user)+"//"}
        self.send(json.dumps(data))

