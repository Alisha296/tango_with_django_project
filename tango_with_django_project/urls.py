"""tango_with_django_project URL Configuration

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from store.views import *  # Import all views from the store app

# Ensure there are no duplicate imports

urlpatterns = [
    # Admin login
    path('admin/login/', auth_views.LoginView.as_view(template_name='admin_login.html'), name='admin_login'),
    
    # Admin site URL
    path('admin/', admin.site.urls),

    # Include URLs from the 'store' app
    path('store/', include('store.urls')),

    # Additional paths for store app functionality
    path('get_product_sizencolor/', get_product_sizencolor, name='get_product_sizencolor'),
    path('get_available_colors/', get_available_colors, name='get_available_colors'),
    path('edit_product_sizencolor/', edit_product_sizencolor, name='edit_product_sizencolor'),
    path('check_stock_quantity/', check_stock_quantity, name='check_stock_quantity'),

    # Admin-side URLs
    path('admin_side/', admin_side, name='admin_side'),
    path('add_category/', add_category, name='add_category'),
    path('add_size/', add_size, name='add_size'),
    path('add_color/', add_color, name='add_color'),
    path('allproduct/', allproduct, name='allproduct'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:id>/', edit_product, name='edit_product'),
    path('edit_quantity/<int:id>/', edit_quantity, name='edit_quantity'),
    path('edit_quantity/getstock/', getstock, name='getstock'),
    path('edit_quantity/getcolor/', getcolor, name='getcolor'),
    path('remove_product/<int:id>/', remove_product, name='remove_product'),
    path('remove_products/<int:id>/', remove_products, name='remove_products'),
    
    # Order-related paths
    path('order_list/', order_list, name='order_list'),
    path('user_list/', user_list, name='user_list'),
    path('product_list/', product_list, name='product_list'),
    path('contact_list/', contact_list, name='contact_list'),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
    path('order_delete/<int:order_id>/', order_delete, name='order_delete'),
    
    # Admin Dashboard
    path('1/', redirect_to_admin, name='redirect_to_admin'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('admin_logout/', admin_logout, name='admin_logout'),
    
    # Customer-facing URLs
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_cus, name='logout'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    
    # Invoice and contact
    path('invoice/<int:order_id>/', invoice, name='invoice'),
    path('generate_invoice/<int:order_id>/', generate_invoice, name='generate_invoice'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    
    # Search and cart
    path('search/', search, name='search'),
    path('cart/', cart, name='cart'),
    path('addcart/<int:id>/', addcart, name='addcart'),
    path('removecart/<int:id>/', removecart, name='removecart'),
    path('updatecart/', updatecart, name='updatecart'),
    path('checkout/', checkout, name='checkout'),
    
    # Address and order-related
    path('address/', address, name='address'),
    path('placeorder/', place_order, name='placeorder'),
    path('order_confirm/<str:hasher_id>/', order_confirm, name='order_confirm'),
    path('order_history/', order_history, name='order_history'),
    path('cancel_order/<int:order_id>/', cancel_order, name='cancel_order'),
    path('return_order/<int:order_id>/', return_order, name='return_order'),
    
    # Product and category-specific URLs
    path('show_product/<int:id>/', show_product, name='show_product'),
    path('<str:cate>/', section, name='section'),
]

# Serve media and static files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom 404 handler
handler404 = "app.views.custom_page_not_found"
