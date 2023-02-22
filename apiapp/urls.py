from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('github/', views.github_api, name = 'github'),
    path('checkout/', views.paypal, name = 'checkout'),
    path('sociallogin/', views.sociallogin, name = 'social-login'),
    path('socialhome/', views.socialhome, name = 'social-home'),
    path('accounthome/', views.accounthome, name = 'accounthome'),
    path('otp_login/', views.otp_login, name = 'otp_login'),
    path('otp_verify/', views.otp_verify, name = 'otp_verify')

]