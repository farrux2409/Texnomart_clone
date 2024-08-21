# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from knox.auth import TokenAuthentication as KnoxTokenAuthentication
from rest_framework import filters, viewsets
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *


# Create your views here.

# Categories CRUD ---->>

# class CategoryList(generics.ListAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [TokenAuthentication, KnoxTokenAuthentication]
#
#     # authentication_classes = [JWTAuthentication]
#     # queryset = Category.objects.all()
#     model = Category
#     serializer_class = CategoryModelSerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filter_fields = ['category_name', ]
#     search_fields = ['category_name', ]
#     ordering_fields = ['category_name', ]
#
#     def get_queryset(self):
#         queryset = Category.objects.prefetch_related('products').all()
#         return queryset
#
#     @method_decorator(cache_page(30))
#     def get(self, *args, **kwargs):
#         return super().get(*args, **kwargs)

class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategoryModelSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'

    def get_queryset(self):
       
        queryset = Category.objects.prefetch_related('products').all()
        return queryset


    @method_decorator(cache_page(10))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = AllCategoriesModelSerializer
    permission_classes = [permissions.AllowAny]

    @method_decorator(cache_page(30))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class CategoryDetailUpdate(generics.RetrieveUpdateAPIView):
    model = Category
    serializer_class = AllCategoriesModelSerializer
    lookup_field = 'slug'

    def get_queryset(self):
       
        queryset = Category.objects.all()
        return queryset


class CategoryDetailDelete(generics.RetrieveDestroyAPIView):
    model = Category
    serializer_class = AllCategoriesModelSerializer
   
    lookup_field = 'slug'

    def get_queryset(self):
       
        queryset = Category.objects.all()
        return queryset


class CategoryUpdate(generics.UpdateAPIView):
    model = Category
    serializer_class = AllCategoriesModelSerializer
   
    lookup_field = 'slug'
    def get_queryset(self):
       
        queryset = Category.objects.all()
        return queryset


class CategoryDelete(generics.DestroyAPIView):
    model = Category
    serializer_class = AllCategoriesModelSerializer
    
    lookup_field = 'slug'

    def get_queryset(self):
       
        queryset = Category.objects.all()
        return queryset


# For all Categories

class AllCategoryList(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication,]
    model = Category
    serializer_class = AllCategoriesModelSerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['category_name', ]
    search_fields = ['category_name', ]
    ordering_fields = ['category_name', ]

    @method_decorator(cache_page(30))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


# Products CRUD ---->

# For All Products

class AllProductList(generics.ListAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    model = Product
    serializer_class = AllProductsModelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['product_name', 'price']
    search_fields = ['product_name', 'price']
    ordering_fields = ['product_name', 'price']

    def get_queryset(self):
        queryset = Product.objects.prefetch_related(
            'users_like',
            'users_like__comment_set').all()
        return queryset

    @method_decorator(cache_page(30))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    # class ProductList(generics.ListAPIView):
    #     permission_classes = [permissions.AllowAny]
    #     authentication_classes = [JWTAuthentication]
    #     # queryset = Product.objects.all()
    #     model = Product
    #     serializer_class = ProductSerializer
    #     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    #     filter_fields = ['product_name', 'price']
    #     search_fields = ['product_name', 'price']
    #     ordering_fields = ['product_name', 'price']
    #
        # def get_queryset(self):
        #     queryset = Product.objects.select_related('category').prefetch_related('attributes', 'product_images',
        #                                                                            'users_like',
        #                                                                            'users_like__comment_set').all()
        #     return queryset


class ProductDetail(generics.RetrieveAPIView):
    model = Product
    serializer_class = ProductSerializer
   
    lookup_field = 'pk'

    def get_queryset(self):
            queryset = Product.objects.select_related('category').prefetch_related('attributes', 'product_images',
                                                                                   'users_like',
                                                                                   'users_like__comment_set').all()
            return queryset


class ProductListCreateView(generics.ListCreateAPIView):
   
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    @method_decorator(cache_page(30))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
    
    def get_queryset(self):
            queryset = Product.objects.select_related('category').prefetch_related('attributes', 'product_images',
                                                                                   'users_like',
                                                                                   'users_like__comment_set').all()
            return queryset


class ProductDetailUpdate(generics.RetrieveUpdateAPIView):
    model = Product
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
            queryset = Product.objects.select_related('category').prefetch_related('attributes', 'product_images',
                                                                                   'users_like',
                                                                                   'users_like__comment_set').all()
            return queryset


class ProductDetailDelete(generics.RetrieveDestroyAPIView):
    model = Product
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
            queryset = Product.objects.select_related('category').prefetch_related('attributes', 'product_images',
                                                                                   'users_like',
                                                                                   'users_like__comment_set').all()
            return queryset


class ProductUpdate(generics.UpdateAPIView):
    model = Product
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
            queryset = Product.objects.select_related('category').prefetch_related('attributes', 'product_images',
                                                                                   'users_like',
                                                                                   'users_like__comment_set').all()
            return queryset


class ProductDelete(generics.DestroyAPIView):
    model = Product
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
            queryset = Product.objects.select_related('category').prefetch_related('attributes', 'product_images',
                                                                                   'users_like',
                                                                                   'users_like__comment_set').all()
            return queryset


# For all Attributes


class AttributeKeysList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    model = Attribute
    serializer_class = AttributeModelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['attribute_name', ]
    search_fields = ['attribute_name', ]
    ordering_fields = ['attribute_name', ]
    queryset = Attribute.objects.all()

    @method_decorator(cache_page(30))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class AttributeValuesList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    model = AttributeValue
    serializer_class = AttributeValueModelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['attribute_value', ]
    search_fields = ['attribute_value', ]
    ordering_fields = ['attribute_value', ]
    queryset = AttributeValue.objects.all()

    @method_decorator(cache_page(30))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class ProductAttributesList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    model = ProductAttribute
    serializer_class = ProductAttributeModelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ['key', 'value']
    search_fields = ['key', 'value']
    ordering_fields = ['key', 'value']
    queryset = ProductAttribute.objects.all()

    def get_queryset(self):
        product_id = self.kwargs['pk']
        return ProductAttribute.objects.filter(product_id=product_id).select_related('key', 'value', 'product')

    @method_decorator(cache_page(30))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


# ModelViewSet
class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field = 'pk'

    @method_decorator(cache_page(30))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = AllCategoriesModelSerializer
    lookup_field = 'pk'

    @method_decorator(cache_page(30))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
