from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('i', views.list_voitures, name='i'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('carsingle', views.carsingle, name='carsingle'),
    path('profil', views.profil, name='profil'),
    path('orders', views.orders, name='orders'),
]