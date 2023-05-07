from django.urls import path 
from . import views


urlpatterns = [
    path('', views.restricted_ipadress_access, name = 'restrictedipadressaccess'),
    path('max-covid19-death-rate/', views.max_covid19_death_rate, name = 'maxcovid19deathrate'),
    path('paypalcheckout/', views.paypalcheckout, name = 'paypalcheckout'),
    path('sociallogin/', views.sociallogin, name = 'social-login'),
    path('otplogin/', views.otp_login, name = 'otplogin'),
]