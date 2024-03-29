from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pizza, Burger

def index(request):
    ctx = {'name': 'welcome to our food'}
    return render(request, 'food/index.html', ctx)

def pizza(request):
    pizzas = Pizza.objects.all()
    ctx = {'pizzas': pizzas}
    return render(request, 'food/pizza.html', ctx)

def burger(request):
    burgers = Burger.objects.all()
    ctx = {'burgers': burgers}
    return render(request, 'food/burger.html', ctx)

def get_pizza_details(request, pizza_id, size):
    try:
        pizza = Pizza.objects.get(id=pizza_id)
        if size == 'medium':
            price = pizza.price_m
        else:
            price = pizza.price_l

        pizza_details = {
            'name': pizza.name,
            'price': price,
            'image': pizza.image.url
        }
        return JsonResponse(pizza_details)
    except Pizza.DoesNotExist:
        return JsonResponse({'error': 'Pizza not found'}, status=404)

def get_burger_details(request, burger_id):
    try:
        burger = Burger.objects.get(id=burger_id)
        burger_details = {
            'name': burger.name,
            'price': burger.price,
            'image': burger.image.url
        }
        return JsonResponse(burger_details)
    except Burger.DoesNotExist:
        return JsonResponse({'error': 'Burger not found'}, status=404)
