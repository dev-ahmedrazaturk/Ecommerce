from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Maps to landing page
    path('cart/', views.cart_page, name='cart_page'),    # Maps to shopping cart
    path('checkout/', views.checkout_page, name='checkout_page'),  # Maps to checkout page
    path('admin/', views.admin_page, name='admin_page'),  # Maps to admin page
]

