# fashion/urls.py
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^men/$', views.men, name='men'),
    url(r'^women/$', views.women, name='women'),
    url(r'^kids/$', views.kids, name='kids'),
    url(r'^product/(?P<product_id>\d+)/$', views.product, name='product'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^search/$', views.search, name='search'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^add-to-cart/(?P<product_id>\d+)/$', views.add_to_cart, name='add_to_cart'),
    url(r'^password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html')),
    url(r'^password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
