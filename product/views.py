from django.shortcuts import render
from .models import Product, ProductCategory

# Create your views here.


def index(request):
    return render(request, 'product/index.html')


def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'category': ProductCategory.objects.all()
            }
    return render(request, 'product/products.html', context=context)
