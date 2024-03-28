from django.urls import path
from . import views

app_name = 'food'  # Add this line to specify the app name

urlpatterns = [
    path('', views.index, name='index'),  # This should point to your index view
    path('pizza/', views.pizza, name='pizza'),  # This is the root URL pattern
]
