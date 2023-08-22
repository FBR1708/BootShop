from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserView, UserActiveView, ProductShopModelViewSet

router = DefaultRouter()

router.register('users', UserView, 'user')
router.register('user', UserActiveView, 'user')
router.register("product/shop", ProductShopModelViewSet, basename="product_shop")

urlpatterns = [
    path('', include(router.urls))
]
