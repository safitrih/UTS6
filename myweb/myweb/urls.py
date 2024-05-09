from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cookies.views import CookieTypeViewSet, CookieViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'cookie-types', CookieTypeViewSet)
router.register(r'cookies', CookieViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
