from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed
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


def pre_save_cart_receiver(sender, instance, action, *args, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        products = instance.products.all()
        total = sum(map(lambda p:p.price, products))
        instance.total = total
        instance.save()


def m2m_save_cart_receiver(sender, instance, action, *args, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        products = instance.products.all()
        total = sum(map(lambda p:p.price, products))
        instance.total = total
        instance.save()


pre_save.connect(pre_save_cart_receiver, Cart.products.through)
m2m_changed.connect(m2m_save_cart_receiver, Cart.products.through)

