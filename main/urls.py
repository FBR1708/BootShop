# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ProductModelViewSet
#
#
# router = DefaultRouter()
# router.register("products", ProductModelViewSet, basename="products")
#
#
# urlpatterns = [
#     path('', include(router.urls))
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import ProductClassViewSet, CategoryClassViewSet, ProductImageViewSet, ProductColorViewSet, \
    IsActiveViewSet

router = DefaultRouter()
router.register('products', ProductClassViewSet, basename='products')
router.register('categories', CategoryClassViewSet, basename='categories')
router.register('images', ProductImageViewSet, basename='images')
router.register('colors', ProductColorViewSet, basename='colors')
router.register('is_active', IsActiveViewSet, basename='is_active')

urlpatterns = [
    path('', include(router.urls))
]
