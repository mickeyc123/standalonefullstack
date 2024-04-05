from email.utils import collapse_rfc2231_value
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Pizza, Burger, Order
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from .forms import RegistrationForm





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
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            house_address = form.cleaned_data['house_address']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            password = form.cleaned_data['password2']


            # Create a new User object
            user = User.objects.create_user(username=username, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            # Redirect to index page after successful registration
            return redirect('food:index')  # Update 'food:index' to your actual index URL name

    else:
        form = RegistrationForm()

    ctx = {'form': form}
    return render(request, 'food/signup.html', ctx)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User is authenticated, log them in
            auth_login(request, user)
            # Redirect to the index page
            return redirect('food:index')  # Assuming 'food' is your app_name
        else:
            # Invalid credentials, show an error message
            error_message = "Invalid username or password."
            ctx = {'error_message': error_message, 'active_link': 'login'}
            return render(request, 'food/login.html', ctx)

    ctx = {'active_link': 'login'}
    return render(request, 'food/login.html', ctx)

