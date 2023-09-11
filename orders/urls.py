from django.urls import path
from .views import SuccerssView, CanceledView
from .views import *


app_name = 'orders'

urlpatterns = [
    path('create/',OrderCreateView.as_view(), name='order_create'),
    path('success/',SuccerssView.as_view(), name='order_success'),
    path('cancel/',CanceledView.as_view(), name='order_canceled'),
]