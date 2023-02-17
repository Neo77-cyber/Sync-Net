from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('github/', views.github_api, name = 'github'),
    path('checkout/', views.paypal, name = 'checkout'),
    path('otptoken/', views.transfer, name= 'transfer')
    
]