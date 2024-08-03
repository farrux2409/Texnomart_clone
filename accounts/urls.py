from . import views
from .views import *
from django.urls import path
app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterUserAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
]