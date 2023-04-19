from django.shortcuts import render, redirect


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
# Create your views here.
