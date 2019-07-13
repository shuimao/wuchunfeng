from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, response, request
from django.template import loader
from .models import *
from django.contrib.auth import login as lgi, logout as lgo, authenticate

from PIL import Image, ImageDraw, ImageFont
import random, io
from django.core.cache import cache
from django.core.mail import send_mail, EmailMultiAlternatives, send_mass_mail
from django.conf import settings
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
        # temp = loader.get_template('booktest2/indexes.html')
        # result = temp.render({})
    # name = request.session.get('name')
    return render(request, 'booktest2/indexes.html', locals())
    # else:
        # return redirect(reverse('booktest2:login'))
    # name = request.COOKIES.get('name')
    # res = HttpResponse('indexes')
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
        # response = redirect(reverse('booktest2:indexes'))
        # response.set_cookie('name', request.POST.get('name'))
        # return response
        # request.session['name'] = request.POST.get('name')
        name = request.POST.get('name')
        password = request.POST.get('password')
        veritycode = request.POST.get('verity')
        # a = cache.get('verity')
        # print(veritycode)
        # print(a)
        if not veritycode == cache.get('verity'):

            return HttpResponse("验证码错误")
        user = authenticate(request, username = name, password= password)
        # print(user)
        # print(user.is_active)
        if user:
            if user.is_active:
                lgi(request, user)
                return render(reverse('booktest2:indexes'))
            else:
                return render(request, 'booktest2/login.html', {'errors': '尚未激活'})
        else:

            return render(request, 'booktest2/login.html', {'errors':'登录失败'})


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
            user.is_active = False
            user.save()
        except:
            user = None
        if user:
            email = request.POST.get('email')
            recvlist = [email]
            try:
                msg = EmailMultiAlternatives('测试2', "<p><a href='http://127.0.0.1:8000/booktest2/active/%s'>点击</a></p>"%(user.id,),
                                             settings.EMAIL_HOST_USER, recvlist)
                msg.content_subtype = 'html'
                msg.send()
                print('成功')
                # send_mail('测试邮件','这是一个测试邮件', settings.EMAIL_HOST_USER, recvlist)
            except Exception as a:
                print(a)

            return redirect(reverse('booktest2:login'))
        else:
            return render(request, 'booktest2/login.html', {'errors':'注册失败'})

def verity(request):
    # 定义变量， 用于画面的背景色、 宽、 高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 25
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
    draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码

    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    cache.set("verity",rand_str)

    # 构造字体对象
    font = ImageFont.truetype('Arvo-Regular', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    # print(rand_str)
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端， MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')


def active(request, id):
    user = get_object_or_404(BookUser, pk=id)
    user.is_active=True
    user.save()
    return redirect(reverse('booktest2:login'))