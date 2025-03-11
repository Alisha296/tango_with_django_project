from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
  products = Products.object.all()
  return render(request, 'store/store.html', {'products': products})

#Create User Authentication
def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
    else:
      form = UserCreationForm()
    return render(request,'store/register.html',{'form':form})
