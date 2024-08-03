from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework import status, viewsets, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.views.decorators.cache import cache_page
from .serializers import CategoryModelSerializer
from rest_framework.response import Response
from .models import Category
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication
from .serializers import *
from .models import *


# Create your views here.
class CategoryList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]

    # authentication_classes = [JWTAuthentication]
    # queryset = Category.objects.all()
    model = Category
    serializer_class = CategoryModelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['category_name', ]
    search_fields = ['category_name', ]
    ordering_fields = ['category_name', ]

    def get_queryset(self):
        queryset = Category.objects.prefetch_related('products').all()
        return queryset

    @method_decorator(cache_page(30))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class ProductList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [JWTAuthentication]
    # queryset = Product.objects.all()
    model = Product
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['product_name', 'price']
    search_fields = ['product_name', 'price']
    ordering_fields = ['product_name', 'price']

    def get_queryset(self):
        queryset = Product.objects.select_related('category').prefetch_related('attributes', 'product_images',
                                                                               'users_like','users_like__comment_set').all()
        return queryset

    @method_decorator(cache_page(30))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
