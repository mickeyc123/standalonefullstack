from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizza/', views.pizza, name='pizza'),
    path('burger/', views.burger, name='burger'),
    path('order/', views.order, name='order'),
    path('submit_order/', views.submit_order, name='submit_order'),  # URL for submit_order view
    path('success/', views.success, name='success'),  # URL for success view
]
