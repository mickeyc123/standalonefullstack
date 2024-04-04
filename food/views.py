from email.utils import collapse_rfc2231_value
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Pizza, Burger, Order
from django.views.decorators.csrf import csrf_exempt


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

def order(request):
    ctx = {'active_link': 'order'}
    return render(request, 'food/order.html', ctx)

def submit_order(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Get the 'note' and 'orders' data from the POST request
        note = request.POST.get('note')
        orders = request.POST.get('orders')

        # In this example, we assume 'orders' is sent as JSON string, so parse it
        import json
        orders_list = json.loads(orders)

        # Create an Order instance and save it (this is a simplified example)
        # You would typically handle the order data according to your models
        # Here, we're just returning a success message
        Order.objects.create(note=note, orders=orders_list)

        # Redirect to the success page
    return render(request, 'food/success.html')



def success(request):
    return render(request, 'food/success.html')
