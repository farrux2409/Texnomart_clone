from django.urls import path, include
from django.urls import path, include
from .views import *

app_name = 'app'

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
    path('products/', ProductList.as_view(), name='products'),
]
