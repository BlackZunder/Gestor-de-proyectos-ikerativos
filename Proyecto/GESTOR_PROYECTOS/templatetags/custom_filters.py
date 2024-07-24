from django import template
import random

register = template.Library()

@register.filter
def random_color(colors):
    colors_list = colors.split()
    return random.choice(colors_list)