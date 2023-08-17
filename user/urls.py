from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'users'

urlpatterns = [
    path('login/',login, name='login'),
    path('registration/',UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/',login_required(UserProfileView.as_view()), name='profile'),
    path('logout/',logout, name='logout'),

]