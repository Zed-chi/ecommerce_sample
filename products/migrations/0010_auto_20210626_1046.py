# Generated by Django 3.1 on 2021-06-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0009_auto_20210626_0119"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(blank=True, default="qwe", unique=True),
        ),
    ]
