# from django.conf import settings
# settings.configure()
from django import template

register = template.Library()


@register.filter(name='split_by_newline')
def split_by_newline(value):
    """
    Returns the value turned into a list.
    """
    value = value.decode('utf-8')
    return value.split('\r\n')


@register.filter(name='convert_list_to_int')
def convert_list_to_int(list_of_values):
    return [int(float(element)) for element in list_of_values]
