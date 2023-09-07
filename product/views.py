from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from common.views import TitleMixin



# Create your views here.


class IndexView(TitleMixin, TemplateView):
    template_name = 'product/index.html'
    title = 'Store'


class ProductListView(TitleMixin, ListView):
    model = Product
    template_name = 'product/products.html'
    paginate_by = 3
    title = 'Store - Каталог'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.kwargs.get('category_id', None)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class BasketView:
    @staticmethod
    @login_required
    def add_basket(request, product_id):
        product = Product.objects.get(id=product_id)
        baskets = Basket.objects.filter(user=request.user, product=product)
        if not baskets.exists():
            Basket.objects.create(user=request.user, product=product, quantity=1)
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()

        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    @staticmethod
    @login_required
    def basket_remove(request, basket_id):
        basket = Basket.objects.get(id=basket_id)
        basket.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


# def index(request):
#     return render(request, 'product/index.html')


# def products(request,category_id=None,page= 1):
#     if category_id:
#         product = Product.objects.filter( category_id=category_id)
#     else:
#         product = Product.objects.all()
#     per_page = 3
#     paginator = Paginator(product, per_page)
#     products_paginator = paginator.page(page)
#     context = {
#         'title': 'Store - Каталог',
#         'products': products_paginator,
#         'category': ProductCategory.objects.all()
#             }
#
#     return render(request, 'product/products.html', context=context)


# @login_required
# def add_basket(request, product_id):
#     product = Product.objects.get(id=product_id)
#     baskets = Basket.objects.filter(user=request.user, product=product)
#     if not baskets.exists():
#         Basket.objects.create(user=request.user, product=product, quantity=1)
#     else:
#         basket = baskets.first()
#         basket.quantity += 1
#         basket.save()
#
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])
#
#
# @login_required
# def basket_remove(request, basket_id):
#     basket = Basket.objects.get(id=basket_id)
#     basket.delete()
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])
