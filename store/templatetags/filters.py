from django import template

register = template.Library()


@register.filter(name='rupees')
def rupees(number):
    return "रू " + str(number)


@register.filter(name='total')
def rupees(number1, number2):
    return number1 * number2
