from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Homepage for the store
    path("category/<slug:slug>/", views.category_products, name="category_products"),
    path('register/',views.register,name='register'),
]
