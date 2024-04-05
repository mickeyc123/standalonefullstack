from email.utils import collapse_rfc2231_value
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Pizza, Burger, Order
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.views.decorators.csrf import csrf_protect



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

        # Create an Order instance but do not save yet
        order = Order(note=note, orders=orders_list)

        # Save the order to the database
        order.save()

        # Here, you can also send a response if needed, such as a success message
        # For example, if using AJAX, you can return JSON response
        return JsonResponse({'message': 'Order submitted successfully!'})

    return render(request, 'food/success.html')

def success(request):
    return render(request, 'food/success.html')

def signup(request):
    ctx = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
        else:
            ctx['form'] = form
    else:
        form = UserCreationForm()
        ctx['form'] = form
    return render(request, 'food/signup.html', ctx)

def login(request):
    ctx = {'active_link': 'login'}
    return render(request, 'food/login.html', ctx)
