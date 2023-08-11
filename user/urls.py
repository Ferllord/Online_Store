from django.urls import path

from .views import *

app_name = 'products'

urlpatterns = [
    path('login/',login, name='login'),
    path('registration/',register, name='register')
]