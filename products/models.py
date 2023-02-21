import os
import random
import time

from django.db import models
from django.db.models.signals import post_save, pre_save

from .util import unique_slug_generator


def get_file_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext


def upload_image_path(inst, filename):
    new_filename = str(time.time_ns())
    _, ext = get_file_ext(filename)
    return f"products/{new_filename}{ext}"


class ProductQuerySet(models.QuerySet):
    def featured(self):
        return self.filter(featured=True, active=True)

    def active(self):
        return self.filter(active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def get_by_id(self, _id):
        qs = self.get_queryset().get(id=_id)
        if qs.count() == 1:
            return qs.first()

    def featured(self):
        return self.get_queryset().featured()

    def all(self):
        return self.get_queryset().active()

    def search(query:str):
        lookups = Q(title__icontains=query) | Q(description__icontains=query)
        return Product.objects.active().filter(lookups).distinct()

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, default="qwe", unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True
    )
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"{self.slug}/"


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
