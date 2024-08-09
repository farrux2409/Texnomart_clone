from django.urls import path, include
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductModelViewSet, basename='product')
router.register(r'categories', CategoryModelViewSet, basename='category')
app_name = 'app'

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    # path('categories1/', CategoryList.as_view(), name='categories'),
    # path('products/', ProductList.as_view(), name='products'),

    # For Categories
    path('categories/', AllCategoryList.as_view(), name='all_categories'),
    # Use Retrieve Views
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/add-category/', CategoryListCreateView.as_view(), name='category_add'),
    path('category/<slug:slug>/delete/', CategoryDetailDelete.as_view(), name='category_delete'),
    path('category/<slug:slug>/edit/', CategoryDetailUpdate.as_view(), name='category_edit'),

    # For Products
    path('', AllProductList.as_view(), name='all_products'),
    # Use Retrieve Views
    path('product/detail/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('product/add-product/', ProductListCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/edit/', ProductDetailUpdate.as_view(), name='product_detail'),
    path('product/<int:pk>/delete/', ProductDetailDelete.as_view(), name='product_detail'),
    # Use Simple Api Views
    path('product-update/<int:pk>/', ProductUpdate.as_view(), name='product_update'),
    path('product-delete/<int:pk>/', ProductDelete.as_view(), name='product_delete'),

    # For Attributes
    path('attribute-key/', AttributeKeysList.as_view(), name='attribute_keys'),
    path('attribute-value/', AttributeValuesList.as_view(), name='attribute_values'),
    path('product/<int:pk>/product-attributes/', ProductAttributesList.as_view(), name='product_attributes'),

    # #     # For JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ModelViewSet
    path('modelviewset-categories/', include(router.urls)),
    path('modelviewset-products/', include(router.urls)),

]
