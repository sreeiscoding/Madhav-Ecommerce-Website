# Generated by Django 4.2 on 2024-12-20 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("home", "0003_alter_gallery_image_alter_product_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, default="shop-image-jpg", upload_to="images"
                    ),
                ),
                ("store_name", models.CharField(blank=True, max_length=120, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "vendor_id",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="12345678890",
                        length=6,
                        max_length=20,
                        prefix="",
                        unique=True,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("slug", models.SlugField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vendor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Payout",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
                ),
                (
                    "payout_id",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="1234567890",
                        length=6,
                        max_length=10,
                        prefix="",
                        unique=True,
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "item",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="item",
                        to="home.orderitem",
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="vendor.vendor",
                    ),
                ),
            ],
            options={"ordering": ["-date"],},
        ),
        migrations.CreateModel(
            name="Notifications",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("New Order", "New Order"),
                            ("Item Shipped", "Item Shipped"),
                            ("Item Delivered", "Item Delivered"),
                        ],
                        default=None,
                        max_length=100,
                    ),
                ),
                ("seen", models.BooleanField(default=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "order",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="home.orderitem",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vendor_notification",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name_plural": "Notification",},
        ),
        migrations.CreateModel(
            name="BankAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "account_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("PayPal", "PayPal"),
                            ("Stripe", "Stripe"),
                            ("Indian Bank Account", "Indian Bank Account"),
                            ("USA Bank Account", "USA Bank Account"),
                        ],
                        max_length=30,
                        null=True,
                    ),
                ),
                ("bank_name", models.CharField(max_length=500)),
                ("account_number", models.CharField(max_length=100)),
                ("account_name", models.CharField(max_length=100)),
                ("bank_code", models.CharField(blank=True, max_length=100, null=True)),
                ("stripe_id", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "paypal_address",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "vendor",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="vendor.vendor",
                    ),
                ),
            ],
            options={"verbose_name_plural": "Bank Account",},
        ),
    ]