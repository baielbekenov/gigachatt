from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('register/', register, name='register'),
    path('login/', loginpage, name='login'),
    path('logout/', logout, name='logout'),
]
