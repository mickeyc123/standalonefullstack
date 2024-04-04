from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.index, name='index'),  # This should point to your index view
    path('pizza/', views.pizza, name='pizza'),  # URL pattern for pizzas
    path('burger/', views.burger, name='burger'),  # URL pattern for burgers
    path('order/', views.order, name='order'),  # URL pattern for rendering the order form
    path('submit_order/', views.submit_order, name='submit_order'),  # URL pattern for submitting the order
]
