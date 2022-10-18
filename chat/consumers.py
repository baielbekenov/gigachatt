import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumers(WebsocketConsumer):
    def connect(self):
        self.room_group_name = self.scope["url_route"]["kwargs"]["pk"]
        print(self.room_group_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected!'
        }))

    def receive(self, text_data):

        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = text_data_json["user"]
        # print(message)
        print(text_data_json['user'])

        print(self.channel_name)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': user,
                'message': message
            }
        )

    def chat_message(self, event):
        print(self.room_group_name)
        message = event['message']
        user = event['user']
        print(user)
        self.send(text_data=json.dumps(
            {
                'type': 'chat',
                'message': message,
                'user': user
            }
        ))
