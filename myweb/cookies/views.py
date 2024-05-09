from rest_framework import viewsets
from .models import CookieType, Cookie, Order
from .serializers import CookieTypeSerializer, CookieSerializer, OrderSerializer

class CookieTypeViewSet(viewsets.ModelViewSet):
    queryset = CookieType.objects.all()
    serializer_class = CookieTypeSerializer

class CookieViewSet(viewsets.ModelViewSet):
    queryset = Cookie.objects.all()
    serializer_class = CookieSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
