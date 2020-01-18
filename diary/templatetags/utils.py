from django import template


register = template.Library()

@register.filter(name="subtract")
def subtract(value, args):
    sub = value - args
    return sub

@register.filter(name="btnfunc")
def btnfunc(value, args):
    args = ',' + str(args) + ','
    if args in value:
        return 'btn-danger'
    else:
        return 'btn-outline-danger'
