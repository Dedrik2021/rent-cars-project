from django.urls import path
from .views import home, about, contact, services

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('contact', contact, name='contact'),

]
