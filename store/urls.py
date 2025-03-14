from django.urls import path
from . import views
from .views import log_request_details

urlpatterns = [
    # URL pattern for the home page
    path("", views.home, name="home"),

    # URL pattern for adding a product
    path('add_product/', views.add_product, name='add_product'),
    
    # URL pattern for editing a product
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
    
    # URL pattern for editing quantity of a product
    path('edit_quantity/<int:id>/', views.edit_quantity, name='edit_quantity'),
    
    # URL pattern for adding a category
    path('add_category/', views.add_category, name='add_category'),
    
    # URL pattern for adding a size
    path('add_size/', views.add_size, name='add_size'),
    
    # URL pattern for adding a color
    path('add_color/', views.add_color, name='add_color'),
    
    # URL pattern for getting the color based on size and product
    path('getcolor/', views.getcolor, name='getcolor'),
    
    # URL pattern for getting the stock quantity based on product, size, and color
    path('getstock/', views.getstock, name='getstock'),
    
    # URL pattern for removing a product
    path('remove_product/<int:id>/', views.remove_product, name='remove_product'),
    
    # URL pattern for viewing all products
    path('allproduct/', views.allproduct, name='allproduct'),
    
    # URL pattern for removing a product from the product list
    path('remove_products/<int:id>/', views.remove_products, name='remove_products'),
    
    # URL pattern for viewing the product list
    path('product_list/', views.product_list, name='product_list'),
    
    # URL pattern for logging out as an admin
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    
    # URL pattern for the admin dashboard
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # URL pattern for viewing the user list
    path('user_list/', views.user_list, name='user_list'),
    
    # URL pattern for viewing the order list
    path('order_list/', views.order_list, name='order_list'),
    
    # URL pattern for viewing the contact list
    path('contact_list/', views.contact_list, name='contact_list'),
    
    # URL pattern for viewing the details of an order
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),

    # URL pattern for logging request details
    path('log-request/', log_request_details, name='log_request_details'),
    
    # URL pattern for deleting an order
    path('order_delete/<int:order_id>/', views.order_delete, name='order_delete'),
]
