from django.conf import settings
from django.urls import include, path

from cart import views

urlpatterns = [
    path("", views.cart_home, name="home"),
]


app_name = "cart"
