from django.conf import settings
from django.db import models

from products.models import Product

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_cart(self, user=None):
        return self.model.objects.create(user=user)
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0, decimal_places=2, max_digits=10)

    objects = CartManager()