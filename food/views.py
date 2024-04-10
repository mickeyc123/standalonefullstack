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
import json
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash







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
        data = json.loads(request.body)
        note = data.get('note')
        address = data.get('address')
        orders = data.get('orders')

        try:
            orders_list = orders
            order = Order.objects.create(note=note, address=address, orders=orders_list)
            order.save()

            return JsonResponse({'message': 'Order submitted successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return redirect('food:success')


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

def logout_view(request):
    logout(request)
    return redirect('food:index')

def edit(request):
    return render(request, 'food/edit.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('food:index')  # Redirect to index page
    else:
        user_form = UserChangeForm(instance=request.user)
    
    return render(request, 'food/edit.html', {'user_form': user_form})

@login_required
def update_profile(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Update session to prevent logout
            return redirect('food:index')  # Redirect to index page
    else:
        password_form = PasswordChangeForm(request.user)
    
    return render(request, 'food/edit.html', {'password_form': password_form})

def delete_account(request):
    if request.method == 'POST':
        # Perform deletion logic here
        user = request.user
        user.delete()
        logout(request)  # Logout the user after deleting the account
        return redirect('food:index')  # Redirect to index or another page
    else:
        # Render a confirmation page if GET request
        return render(request, 'food/edit.html')