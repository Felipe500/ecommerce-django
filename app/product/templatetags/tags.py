from django.template import Library
from app.common import utils

register = Library()


@register.filter
def format_price(val):
    return utils.format_price_(float(val))


@register.filter
def cart_total_qtd(carrinho):
    return utils.cart_total_qtd(carrinho)


@register.filter
def cart_totals(carrinho):
    return utils.cart_totals(carrinho)
