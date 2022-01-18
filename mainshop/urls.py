from django.contrib import admin
from django.urls import path

from . import views

app_name = 'mainshop'
urlpatterns = [
    path('', views.main, name='index'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
]