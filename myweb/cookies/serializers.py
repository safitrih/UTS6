from rest_framework import serializers
from .models import CookieType, Cookie, Order

class CookieTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookieType
        fields = '__all__'

class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
