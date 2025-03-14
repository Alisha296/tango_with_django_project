from django.urls import path
from . import views
from .views import log_request_details

urlpatterns = [
    path("", views.home, name="home"),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
    path('edit_quantity/<int:id>/', views.edit_quantity, name='edit_quantity'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_size/', views.add_size, name='add_size'),
    path('add_color/', views.add_color, name='add_color'),
    path('getcolor/', views.getcolor, name='getcolor'),
    path('getstock/', views.getstock, name='getstock'),
    path('remove_product/<int:id>/', views.remove_product, name='remove_product'),
    path('allproduct/', views.allproduct, name='allproduct'),
    path('remove_products/<int:id>/', views.remove_products, name='remove_products'),
    path('product_list/', views.product_list, name='product_list'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_list/', views.user_list, name='user_list'),
    path('order_list/', views.order_list, name='order_list'),
    path('contact_list/', views.contact_list, name='contact_list'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order_delete/<int:order_id>/', views.order_delete, name='order_delete'),
    path('log-request/', log_request_details, name='log_request_details'),
]
