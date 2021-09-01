from django import template

register = template.Library()

@register.filter(name = 'is_in_order')
def is_in_order(product, order):
    keys = order.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False                        