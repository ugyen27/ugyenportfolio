from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

def home(request):
  return render(request,'myweb/index.html')

def about(request):
  return render(request, 'myweb/about.html')

def gallery(request):
  return render(request, 'myweb/gallery.html')

def services(request):
  return render(request, 'myweb/services.html')
def contact(request):
  return render(request, 'myweb/contact.html')

