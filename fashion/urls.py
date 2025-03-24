# fashion/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^men/$', views.men, name='men'),
    url(r'^women/$', views.women, name='women'),
    url(r'^kids/$', views.kids, name='kids'),
    url(r'^product/(?P<product_id>\d+)/$', views.product, name='product'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^search/$', views.search, name='search'),
]