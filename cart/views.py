from django.shortcuts import render
from .models import Cart


def cart_home(req):
    cart_id = req.session.get("cart_id", None)
    if not cart_id:        
        cart = Cart.objects.create(user=req.user)
        req.session["cart_id"] = cart.id        
    else:        
        cart = Cart.objects.get(pk=cart_id)
    return render(req, "cart/home.html")
