from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Product

# Get all products from the database

def landing_page(request):
    products = Product.objects.all()  
    return render(request, 'shop/landing_page.html', {'products': products})


# Get cart items from session or other storage
def cart_page(request):
    cart_items = request.session.get('cart', [])
    products_in_cart = Product.objects.filter(id__in=cart_items)  # Fetch products in cart from the DB
    return render(request, 'shop/cart_page.html', {'products_in_cart': products_in_cart})


# Calculate total price
def checkout_page(request):
    cart_items = request.session.get('cart', [])
    products_in_cart = Product.objects.filter(id__in=cart_items)
    total_price = sum(product.price for product in products_in_cart)  
    return render(request, 'shop/checkout_page.html', {'products_in_cart': products_in_cart, 'total_price': total_price})


# Ensure only admins can access this page
# Retrieve all products for admin
@staff_member_required  
def admin_page(request):
    products = Product.objects.all()  
    return render(request, 'shop/admin_page.html', {'products': products})

