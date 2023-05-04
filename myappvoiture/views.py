from django.shortcuts import render, redirect

from myappvoiture.models import *


def index(request):
    return render(request,'test.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def carsingle(request):
    return render(request,'carsingle.html')

def profil(request):
    return render(request,'Profil.html')
def orders(request):
    return render(request,'orders.html')
def list_voitures(request):
    voitures = Voiture1.objects.all()
    return render(request,'test.html',{'voitures':voitures})
# Create your views here.
