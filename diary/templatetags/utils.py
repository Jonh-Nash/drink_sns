from django import template


register = template.Library()

@register.filter(name="subtract")
def subtract(value, args):
    sub = value - args
    return sub