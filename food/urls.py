from django.urls import path
from . import views

app_name = 'food'  # Add this line to specify the app name

urlpatterns = [
    path('', views.index, name='index'),  # This should point to your index view
    path('pizza/', views.pizza, name='pizza'),  # URL pattern for pizzas
    path('burger/', views.burger, name='burger'),  # URL pattern for burgers
    path('get_pizza_details/<int:pizza_id>/<str:size>/', views.get_pizza_details, name='get_pizza_details'),  # URL pattern for getting pizza details
    path('get_burger_details/<int:burger_id>/', views.get_burger_details, name='get_burger_details'),  # URL pattern for getting burger details
]
