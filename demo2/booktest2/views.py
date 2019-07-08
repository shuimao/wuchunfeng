from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, response, request
from django.template import loader
from .models import *
from django.contrib.auth import login as lgi, logout as lgo, authenticate
# Create your views here.
def checklogin(fun):

    def check(request, *args):
        # name = request.COOKIES.get('name')
        # name = request.session.get('name')
        # if name:
        if request.user and request.user.is_authenticated:
            return fun(request, *args)
        else:
            return redirect(reverse('booktest2:login'))
    return check




@checklogin
def index(request):
    # name = request.COOKIES.get('name')
    # print('当前用户为', name)
    # if name:
        # temp = loader.get_template('booktest2/index.html')
        # result = temp.render({})
    # name = request.session.get('name')
    return render(request, 'booktest2/index.html', locals())
    # else:
        # return redirect(reverse('booktest2:login'))
    # name = request.COOKIES.get('name')
    # res = HttpResponse('index')
    # res.set_cookie('name', 'abc')
    # return res

@checklogin
def list(request):
    temp = loader.get_template('booktest2/list.html')
    books = Books.objects.all()
    result = temp.render({'books':books})
    return HttpResponse(result)

@checklogin
def detail(request, id):
    temp = loader.get_template('booktest2/detail.html')
    book = Books.objects.get(pk=id)
    result = temp.render({'book':book})
    return HttpResponse(result)

def roledel(request, id):
    temp = loader.get_template('booktest2/roledel.html')
    # result = temp.render({'a':'成功'})
    ro = role.objects.get(pk=id)
    ro.delete()
    # ro.save()
    bookid = ro.book.id
    # return HttpResponse(result)
    return redirect(reverse('booktest2:detail', args=(bookid,)))

def roleadd(request, id):
    book = Books.objects.get(pk=id)
    if request.method == 'GET':
        temp = loader.get_template('booktest2/roleadd.html')
        result = temp.render({'book':book})
        return HttpResponse(result)
    elif request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        weapon = request.POST.get('weapon')
        r = role()
        r.rolename = name
        r.content = content
        r.weapon = weapon
        r.book = book
        r.save()
        return redirect(reverse('booktest2:detail', args=(book.id,)))


def login(request):
    if request.method == 'GET':
        return render(request, 'booktest2/login.html')
    elif request.method == 'POST':
        # response = redirect(reverse('booktest2:index'))
        # response.set_cookie('name', request.POST.get('name'))
        # return response
        # request.session['name'] = request.POST.get('name')
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username = name, password= password)
        if user:
            lgi(request, user)
            return redirect(reverse('booktest2:index'))
        else:

            return redirect(request, 'booktest2/login.html', {'errors':'登录失败'})


def logout(request):
    # res = redirect(reverse('booktest2:login'))
    # res.delete_cookie('name')
    # return res
    # request.session.flush()
    lgo(request)
    return redirect(reverse('booktest2:login'))

def regist(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password =request.POST.get('password')
        # user = BookUser.objects.create_user(username=name, password=password)
        try:
            user = BookUser.objects.create_user(username=name, password=password)
        except:
            user = None
        if user:
            return redirect(reverse('booktest2:login'))
        else:
            return render(request, 'booktest2/login.html', {'errors':'注册失败'})