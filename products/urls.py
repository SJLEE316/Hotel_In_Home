from django.urls import path
from .views import *

app_name="products"
urlpatterns=[
    path('product_list', product_list, name="product_list"),
]