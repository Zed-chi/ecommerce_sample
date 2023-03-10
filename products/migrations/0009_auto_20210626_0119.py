# Generated by Django 3.1 on 2021-06-25 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_product_featured"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(blank=True, default="qwe"),
        ),
    ]
