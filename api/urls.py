from django.urls import path

from .views import *

app_name = 'api'

urlpatterns = [
    path('product/list', ProductViewList.as_view()),
    path('basket/list', BasketViewList.as_view()),
    path('signup',signup),
    path('get_token',get_token),

]