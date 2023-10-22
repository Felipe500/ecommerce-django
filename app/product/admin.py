from django.contrib import admin
from .models import Product, VariationProduct


class VariationProductInline(admin.TabularInline):
    model = VariationProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [VariationProductInline]
    list_display = ['id', 'name', 'description_short', 'get_price_format', 'get_price_promotional_format']


admin.site.register(VariationProduct)
