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
    return [int(float(element)) for element in list_of_values if element.replace('.','',1).isdigit()]


@register.filter(name='get_time_vector')
def get_time_vector(list_of_values):
    return list(range(len(list_of_values)))


@register.filter(name='convert_to_charts')
def convert_to_charts(list_of_values):
    time_vector = get_time_vector(list_of_values)
    return list([time, value] for time, value in zip(time_vector, list_of_values))


@register.filter(name='get_max_value')
def get_max_value(signal):
    return max(signal)


@register.filter(name='get_min_value')
def get_min_value(signal):
    return min(signal)
