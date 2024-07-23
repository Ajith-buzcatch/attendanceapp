from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/countdown/', consumers.CountdownConsumer.as_asgi()),
]
