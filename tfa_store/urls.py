from django.urls import path
from . import views
urlpatterns = [
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:id>/', views.edit_product, name='edit_product'),
    path('edit-quantity/<int:id>/', views.edit_quantity, name='edit_quantity'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-size/', views.add_size, name='add_size'),
    path('add-color/', views.add_color, name='add_color'),
    path('getcolor/', views.getcolor, name='getcolor'),
    path('getstock/', views.getstock, name='getstock'),
    path('remove-product/<int:id>/', views.remove_product, name='remove_product'),
    path('all-products/', views.allproduct, name='allproduct'),
    path('remove-products/<int:id>/', views.remove_products, name='remove_products'),
    path('product-list/', views.product_list, name='product_list'),
    path('admin-side/', views.admin_side, name='admin_side'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('user-list/', views.user_list, name='user_list'),
    path('order-list/', views.order_list, name='order_list'),
    path('contact-list/', views.contact_list, name='contact_list'),
    path('order-detail/<int:order_id>/', views.order_detail, name='order_detail'),
]