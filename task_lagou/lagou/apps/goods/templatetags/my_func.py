from django.template import library

register = library.Library()

from goods.models import *

@register.simple_tag
def bytype(num = 3):
    return TypeInfo.objects.all()