from django.conf import settings
from django.urls import include, path

from main import views
from products.views import (ProductDetailSlugView, ProductDetailView,
                            ProductListView)

urlpatterns = [
    path("about", views.about_page, name="about"),
    path("contacts", views.contact_page, name="contacts"),
    path("login", views.login_page, name="login"),
    path("register", views.register_page, name="register"),
    path("", views.homepage, name="home"),
]


app_name = "main"
