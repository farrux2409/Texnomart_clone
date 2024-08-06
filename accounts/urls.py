from . import views
from .views import *
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterUserAPI.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login2'),
    # knox login
    path('login1/', LoginAPI.as_view(), name='login'),
]
