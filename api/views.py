from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from .serialisers import ProductSerializer, BasketSerializer
from product.models import Product, Basket
from rest_framework.parsers import JSONParser
from user.models import User
from django.http import JsonResponse


class ProductViewList(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class BasketViewList(generics.ListAPIView):
    serializer_class = BasketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user).all()


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['username'], password=data['password'])
            user.save()
            return JsonResponse({'token': 'qweqweqweqwewq'}, status=201)
        except:
            return JsonResponse({'error': 'Username is already taken'}, status=201)
