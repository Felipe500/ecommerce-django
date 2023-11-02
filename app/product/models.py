import os
import uuid
from PIL import Image

from django.conf import settings
from django.db import models
from django.utils.text import slugify

from app.common.utils import ImageField
from app.common.format import format_price_


class Product(models.Model):
    code = models.UUIDField(editable=False, blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name='Nome')
    description_short = models.TextField(max_length=255, verbose_name='Descrição curta')
    description_long = models.TextField(verbose_name='Descrição longa')
    image = ImageField(upload_to='product_images/%y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    price_marketing = models.FloatField(default=0, verbose_name='Preço')
    price_marketing_promotional = models.FloatField(default=0, verbose_name='Preço Promo.')
    type = models.CharField(default='V', max_length=1, choices=(
        ('V', 'Variável'),
        ('S', 'Simples'),
    ))

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name

    @property
    def get_price_format(self):
        return format_price_(self.price_marketing)
    get_price_format.fget.short_description = 'Preço'

    @property
    def get_price_promotional_format(self):
        return format_price_(self.price_marketing_promotional)
    get_price_promotional_format.fget.short_description = 'Preço Promo.'

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)

        current_width, current_height = img_pil.size
        new_height = round((new_width * current_height) / current_width)

        if new_width >= current_width:
            img_pil.close()
            return
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(img_full_path, optimize=True, quality=65)
        img_pil.close()

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = uuid.uuid4()
        if not self.slug:
            self.slug = f'{slugify(self.name[:20] + str(self.code)[:14])}'
        super().save(*args, **kwargs)

        if self.image:
            self.resize_image(self.image, 800)


class VariationProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, blank=True, null=True)
    price = models.FloatField()
    price_promotional = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Variação do produto'
        verbose_name_plural = 'Variações dos produtos'

    def __str__(self):
        return self.name or self.product.name

