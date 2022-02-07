from django.urls import path
from mainapp import views as mainapp


app_name = 'products'

urlpatterns = [
    path('', mainapp.products, name='products'),
    path('<int:pk>/', mainapp.products, name='category'),
    path('<int:pk>/<int:page>/', mainapp.products, name='product_paginate'),
    path('product/<int:pk>/', mainapp.product, name='product'),

    # path('home/', mainapp.products_home, name='products_home')
    # path('modern/', mainapp.products_modern, name='products_modern'),
    # path('office/', mainapp.products_office, name='products_office'),
    # path('classic/', mainapp.products_classic, name='products_classic')
]
