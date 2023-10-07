from rest_framework import serializers

from product.models import Product
from product.models import Basket


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity')
