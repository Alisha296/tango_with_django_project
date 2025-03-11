from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
  products = Products.object.all()
  return render(request, 'store/store.html', {'products': products})
