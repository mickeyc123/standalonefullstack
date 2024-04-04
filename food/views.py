from email.utils import collapse_rfc2231_value
from django.shortcuts import render
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
    # Set session expiry
    request.session.set_expiry(0)
    
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # This is an AJAX POST request
        note = request.POST.get('note')
        orders = request.POST.get('orders')

        request.session['note'] = note
        request.session['orders'] = orders

        # You can add additional logic here if needed
        
        # Return a success message
        return JsonResponse({'message': 'Order successfully submitted'})

    # If it's not an AJAX request, return an error
    return JsonResponse({'error': 'Invalid request'})