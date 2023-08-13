from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [
    path('login/',login, name='login'),
    path('registration/',register, name='register'),
    path('profile/',profile, name='profile'),
    path('logout/',logout, name='logout'),

]