from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KainBatikViewSet

router = DefaultRouter()
router.register(r'kainbatik', KainBatikViewSet)

urlpatterns = [
    path('', include(router.urls)),
]