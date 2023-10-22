from django.contrib import admin
from .models import Product, VariationProduct


class VariationProductInline(admin.TabularInline):
    model = VariationProduct
    extra = 1


@admin.register(Product)
class BusinessAdmin(admin.ModelAdmin):
    inlines = [VariationProductInline]

admin.site.register(VariationProduct)
