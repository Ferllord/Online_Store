from rest_framework import generics, permissions
from .serialisers import ProductSerializer
from product.models import Product

class ProductViewList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

