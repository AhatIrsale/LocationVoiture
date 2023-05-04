from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.list_voitures, name='i'),
    path('car/<int:pk>/',CarDetail.as_view(),name = "cardetail"),
    path('list', views.index, name='list'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('carsingle', views.carsingle, name='carsingle'),
    path('profil', views.profil, name='profil'),
    path('orders', views.orders, name='orders'),
]