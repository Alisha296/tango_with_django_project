from django.shortcuts import render
from .models import Product
# Create your views here.


def home(request):
    return render(request, 'fashion/home.html')

def men(request):
    return render(request, 'fashion/men.html')

def women(request):
    return render(request, 'fashion/women.html')

def kids(request):
    return render(request, 'fashion/kids.html')

def product(request, product_id):
    return render(request, 'fashion/product.html', {'product_id': product_id})

def cart(request):
    return render(request, 'fashion/cart.html')

def contact(request):
    return render(request, 'fashion/contact.html')

def search(request):
    return render(request, 'fashion/search.html')