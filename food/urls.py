from django.urls import path
from . import views

app_name = 'food'  # Add this line to specify the app name

urlpatterns = [
    path('', views.index, name='index.html'),  # This is the root URL pattern
    path('pizza/', views.pizza, name='pizza'),
]
