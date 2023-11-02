from django.template import Library
from app.common.format import format_price_
register = Library()


@register.filter
def format_price(val):
    print(val)
    if not val:
        print('not val')
    return format_price_(float(val))
