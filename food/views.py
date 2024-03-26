from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ctx = {'name': 'good food'}  # Corrected context dictionary
    return render(request, 'food/index.html', ctx)  # Using render instead of HttpResponse

def pizza(request):
    return render(request, 'food/pizza.html')

