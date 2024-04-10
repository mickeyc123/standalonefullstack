from django.urls import path
from . import views
from django. contrib import admin

app_name = 'food'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizza/', views.pizza, name='pizza'),
    path('burger/', views.burger, name='burger'),
    path('order/', views.order, name='order'),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('food/success/', views.success, name='food/success'),  
    path('signup/', views.signup, name='signup'), 
    path('login/', views.login, name='login'),  
    path('admin/', admin.site.urls),
    path('logout/', views.logout_view, name='logout'),  
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete_account, name='delete_account'),


]


