import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class CountdownConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'countdown'
        self.room_group_name = 'countdown_group'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        remaining_time = data['remaining_time']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'update_countdown',
                'remaining_time': remaining_time
            }
        )

    def update_countdown(self, event):
        remaining_time = event['remaining_time']

        self.send(text_data=json.dumps({
            'remaining_time': remaining_time
        }))
