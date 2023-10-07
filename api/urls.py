from django.urls import path

from .views import *

app_name = 'api'

urlpatterns = [
    path('product/list', ProductViewList.as_view()),
]