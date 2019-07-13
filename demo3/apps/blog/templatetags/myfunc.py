
from django.template import library
register = library.Library()
from blog.models import *

@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.order_by("-create_time")[:num]


@register.filter
def myjoin(value, split):
    return split.join(value)

@register.simple_tag
def bytime(num=3):
    return Article.objects.dates("create_time", "month", order="DESC")[:num]

@register.simple_tag
def bycategory(num=3):
    return Category.objects.all()[:num]

@register.simple_tag
def bytag():
    return Tag.objects.all()

