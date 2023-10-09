from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from .serialisers import ProductSerializer, BasketSerializer
from product.models import Product, Basket
from rest_framework.parsers import JSONParser
from user.models import User
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


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
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except:
            return JsonResponse({'error': 'Username is already taken'}, status=201)

@csrf_exempt
def get_token(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username =data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error': 'Username is already taken'}, status=201)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=200)
