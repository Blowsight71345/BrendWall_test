from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Заполните название товара.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена должна быть положительным числом и не может быть равна 0.")
        return value
