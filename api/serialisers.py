from rest_framework import serializers

from product.models import Product
from product.models import Basket


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity')



class BasketSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    class Meta:
        model = Basket
        fields = ('id', 'product','product_name', 'quantity')
