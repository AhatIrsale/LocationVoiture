from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView

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
def register(request):
    return render(request,'Signup.html')



def list_voitures(request):
    print("hi")
    client_id = request.session.get('client_id')
    print(client_id)
    if client_id is not None:
        client = Client1.objects.get(id=client_id)
        voitures = Voiture1.objects.all()
        return render(request, 'test.html', {'client': client,'voitures':voitures})
    else:
        return redirect('login')  # Replace 'login' with your desired URL



class CarDetail(DetailView):
    model = Voiture1
    template_name = 'carsingle.html'
    context_object_name = 'car'


def logout_view(request):
    request.session['client_id']=None
    return redirect('/login')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        pn = request.POST['phone']
        client = Client1(Username=name,email=email, Pswd=password,Phone=pn,Language=None,HourFormat=None)
        client.save()
        return redirect('login')
    else:
        return render(request, 'Signup.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            client = Client1.objects.get(email=email)
            if client.check_password(password):
                request.session['client_id'] = client.id
                context = {'Succes': ''}

                return redirect('profil')
        except Client1.DoesNotExist:
            context = {'error': 'Invalid email or password'}
            return render(request, 'Login.html', context)
    return render(request, 'Login.html')

# Create your views here.
