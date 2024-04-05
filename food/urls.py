from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizza/', views.pizza, name='pizza'),
    path('burger/', views.burger, name='burger'),
    path('order/', views.order, name='order'),
    path('submit_order/', views.submit_order, name='submit_order'),  
    path('success/', views.success, name='success'),  
    path('signup/', views.signup, name='signup'), 
    path('login/', views.login, name='login'),  # Corrected name for the login URL
]
