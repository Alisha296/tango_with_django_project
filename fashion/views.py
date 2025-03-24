from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required  
from .models import Product, Cart, CartItem
from .forms import RegistrationForm
# Create your views here.

def get_user_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        return cart
    return None

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
    print(f"User authenticated: {request.user.is_authenticated}")
    print(f"User: {request.user}")
    cart = get_user_cart(request)
    total = 0
    if cart:
        for item in cart.items.all():
            total += float(item.product.price) * item.quantity
    return render(request, 'fashion/cart.html', {'cart': cart, 'total': total})

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

@login_required
def profile(request):
    return render(request, 'fashion/profile.html', {'user': request.user})

def login_view(request):
    print(f"Request method: {request.method}")
    if request.method == 'POST':
        print("POST data:", request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(f"User authenticated: {user}")
        if user is not None:
            login(request, user)
            print(f"Session ID after login: {request.session.session_key}")
            return redirect('home')
        else:
            print("Authentication failed")
            return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
    else:
        print("Rendering login page (GET request)")
    return render(request, 'registration/login.html')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_user_cart(request)
    if cart:
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    return redirect('cart')