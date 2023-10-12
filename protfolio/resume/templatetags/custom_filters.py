from django import template

register = template.Library()

@register.filter(name='split_title')
def split_title(value):
    return value.split(' ')