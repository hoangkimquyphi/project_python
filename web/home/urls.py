from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.get_home, name='home' ),
    path('product-Detail/', views.productDetail, name ="productDetail"),
    
]