from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product


def get_cart(req):
    cart_id = req.session.get("cart_id", None)    
    if not cart_id:        
        cart = Cart.objects.create(user=req.user)
        req.session["cart_id"] = cart.id
        print(f"=== {cart}")  
    else:        
        cart = Cart.objects.get(pk=cart_id)
        print(f"=== {cart} exists")  
    return cart


def cart_home(req):
    cart = get_cart(req)
    print(f"=== {cart} got")  
    return render(req, "cart/home.html", {"cart":cart})


def cart_update(req):
    product_id = req.GET.get("product_id")
    product = Product.objects.get(pk=product_id)    
    cart = get_cart(req)
    if product not in cart.products:
        cart.products.add(product)  
    else:
        cart.products.remove(product)
    req.session["cart_items"] = cart.products.count()  
    return redirect("cart:home")
