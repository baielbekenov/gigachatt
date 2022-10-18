from django.urls import re_path, path
from .consumers import *

websocket_urlpatterns = [
    path('ws/socket-server/<str:pk>', ChatConsumers.as_asgi()),
]