from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza, Burger

# Create your views here.
def index(request):
    ctx = {'name': 'welcome to our food'}  # Corrected context dictionary
    return render(request, 'food/index.html', ctx)  # Using render instead of HttpResponse

def pizza(request):
    pizzas = Pizza.objects.all()  
    ctx = {'pizzas': pizzas}  
    return render(request, 'food/pizza.html', ctx)  

def burger(request):
    burgers = Burger.objects.all()  # Corrected variable name 'burgers'
    ctx = {'burgers': burgers}  # Corrected context dictionary key
    return render(request, 'food/burger.html', ctx)  # Corrected template name
