# Generated by Django 4.2.6 on 2023-11-13 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("qtd_total", models.PositiveIntegerField()),
                ("total", models.FloatField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "Criado"),
                            ("pending", "Pendente"),
                            ("paid", "Aprovado"),
                            ("sent", "Enviado"),
                            ("completed", "Completo"),
                            ("failed", "Reprovado"),
                        ],
                        default="created",
                        max_length=10,
                    ),
                ),
                (
                    "shopper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Pedido",
                "verbose_name_plural": "Pedidos",
            },
        ),
        migrations.CreateModel(
            name="ItemOrder",
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
                ("product_name", models.CharField(max_length=255)),
                ("product_id", models.PositiveIntegerField()),
                ("variation", models.CharField(max_length=255)),
                ("variation_id", models.PositiveIntegerField()),
                ("price", models.FloatField(default=0)),
                ("price_promotional", models.FloatField()),
                ("amount", models.PositiveIntegerField()),
                ("image", models.ImageField(upload_to="")),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="order.order"
                    ),
                ),
            ],
            options={
                "verbose_name": "Item do pedido",
                "verbose_name_plural": "Itens do pedido",
            },
        ),
    ]
