from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import *

def index(responses):
    # return HttpResponse('首页'  "<a href = '/booktest/list/'>列表页</a>")
    temp1 = loader.get_template("booktest/index.html")
    books = BookInfo.objects.all()
    result = temp1.render({'books':books })
    return HttpResponse(result)

def list(responses, id):
    # return HttpResponse('列表'  "<a href = '/booktest/detail/1/'>详情页</a>")
    temp = loader.get_template('booktest/list.html')
    book = BookInfo.objects.get(pk=id)
    result = temp.render({'book':book})
    return HttpResponse(result)
def detail(responses, id):
    # return HttpResponse(" 详情%s  <a href = '/booktest/index/'>主页</a>" %(id,))
    temp = loader.get_template("booktest/detail.html")
    hero = HeroInfo.objects.get(pk=id)
    result = temp.render({'hero':hero})
    return HttpResponse(result)

