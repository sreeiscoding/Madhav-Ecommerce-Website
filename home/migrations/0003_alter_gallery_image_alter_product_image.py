# Generated by Django 4.2 on 2024-12-10 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_rename_carts_cart_rename_orderitems_orderitem_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="image",
            field=models.ImageField(upload_to="images"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
    ]
