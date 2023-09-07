from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

app_name = 'products'

urlpatterns = [
    path('',ProductListView.as_view(), name='list'),
    path('category/<int:category_id>/', ProductListView.as_view(), name='category'),
    path('page/<int:page>/', ProductListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', BasketView.add_basket, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', BasketView.basket_remove, name='basket_remove'),
]
