from django.shortcuts import render,redirect,reverse

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import View,ListView

class ListView(ListView):
    model = BookInfo
    template_name = "booktest/indexes.html"
    context_object_name = "books"
    def get_queryset(self):
        return BookInfo.objects.all()[0:1]



# def indexes(responses):
#     # return HttpResponse('首页'  "<a href = '/booktest/list/'>列表页</a>")
#     temp1 = loader.get_template("booktest/indexes.html")
#     books = BookInfo.objects.all()
#     result = temp1.render({'books':books })
#     return HttpResponse(result)

def list(request, id):
    # return HttpResponse('列表'  "<a href = '/booktest/detail/1/'>详情页</a>")
    temp = loader.get_template('booktest/list.html')
    book = BookInfo.objects.get(pk=id)
    result = temp.render({'book':book})
    return HttpResponse(result)
def detail(responses, id):
    # return HttpResponse(" 详情%s  <a href = '/booktest/indexes/'>主页</a>" %(id,))
    temp = loader.get_template("booktest/detail.html")
    hero = HeroInfo.objects.get(pk=id)
    result = temp.render({'hero':hero})
    return HttpResponse(result)

def deletehero(request, id):
    temp = loader.get_template('booktest/deletehero.html')

    hero = HeroInfo.objects.get(pk=id)
    he1 = hero.book.id
    hero.delete()
    # return HttpResponse('成功')
    return redirect( reverse('booktest:list',args=(he1,)))

def addhero(request, id):
    # return HttpResponse('成功')
    book = BookInfo.objects.get(pk=id)
    if request.method == 'GET':

        return render(request, 'booktest/addhero.html', {'book': book})
    elif request.method == 'POST':
        name = request.POST.get('heroname')
        content = request.POST.get('content')
        gender = request.POST.get('gender')
        rate = request.POST.get('rate')
        hero = HeroInfo()
        hero.heroname = name
        hero.herocontent = content
        hero.herogender = gender
        hero.herorate = rate
        hero.book = book
        hero.save()
        return redirect(reverse("booktest:list", args=(id,)))
        # return HttpResponse('添加成功')

    # book = BookInfo.objects.get(pk=id)

def addbook(request):
    # return HttpResponse('成功')
    if request.method == 'GET':
        return render(request,'booktest/addbook.html')
    elif request.method == 'POST':
        bookname = request.POST.get('bookname')
        book = BookInfo()
        book.title =bookname
        book.save()
        return redirect(reverse("booktest:indexes"))

