from django.shortcuts import render


# Create your models here.
def cart_home(req):
    req.session["cart_id"] = req.user
    req.session["user"] = req.user.username
    return render(req, "cart/home.html")
