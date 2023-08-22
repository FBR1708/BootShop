from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserView, UserActiveView

router = DefaultRouter()

router.register('users', UserView, 'user')
router.register('user', UserActiveView, 'user')

urlpatterns = [
    path('', include(router.urls))
]
