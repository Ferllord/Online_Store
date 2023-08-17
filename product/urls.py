from django.urls import path

from .views import *

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('category/<int:category_id>/', ProductListView.as_view(), name='category'),
    path('page/<int:page>/', ProductListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', add_basket, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
