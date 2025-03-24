from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required  
from .models import Product
from .forms import RegistrationForm
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

@login_required
def cart(request):
    return render(request, 'fashion/cart.html')

def contact(request):
    return render(request, 'fashion/contact.html')

def search(request):
    return render(request, 'fashion/search.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})