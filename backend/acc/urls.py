from django.urls import path
from .views import get_client,create_client,client_detail,get_products,create_products,products_details



urlpatterns = [

path('client/',get_client,name="getClient"),
path('client/create/',create_client,name="createClient"),
path('client/<int:pk>/',client_detail,name="clientDetails"),
path('store/products/',get_products,name="getProducts"),
path('store/products/create/',create_products,name="createProducts"),
path('store/products/<int:pk>/',products_details,name="productDetails"),

]