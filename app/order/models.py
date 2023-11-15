from django.db import models
from django.contrib.auth.models import User
from app.common.choices import ORDER_STATUS


class Order(models.Model):
    shopper = models.ForeignKey(User, on_delete=models.CASCADE)
    qtd_total = models.PositiveIntegerField()
    total = models.FloatField()
    status = models.CharField(default=ORDER_STATUS.created, max_length=10, choices=ORDER_STATUS)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'Pedido N. {self.pk}'


class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=255)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField(default=0)
    price_promotional = models.FloatField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField()

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'

    def __str__(self):
        return f'Item do Pedido {self.order}'
