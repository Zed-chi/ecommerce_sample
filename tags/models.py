from django.db import models
from django.db.models.signals import post_save, pre_save

from products.models import Product
from products.util import unique_slug_generator


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    active = models.BooleanField()
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title


def tag_pre_save_receiver(sender, instance, *atgs, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
