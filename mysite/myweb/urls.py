from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('gallery/',views.gallery, name='gallery'),  #gallery == project
    path('services/',views.services, name='services'),      #services
    path('contact/',views.contact, name='contact')
]