from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),

    path('register/', register, name='register'),
    path('login/', loginpage, name='login'),
    path('logout/', logout, name='logout'),
    path('feedback/', feedback),
    path('feedbacklist/', feedbacklist),

    path('<int:pk>', index2)
# >>>>>>> 9ed58853aef5197b880d5c1837bcfecdcf04e130
]
