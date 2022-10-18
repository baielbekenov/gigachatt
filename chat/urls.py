from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('<int:pk>', index2)
]
