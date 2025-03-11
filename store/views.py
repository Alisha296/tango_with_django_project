from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
  products = Products.object.all()
  return HttpResponse("<h1>Welcome to the Store!</h1>")
