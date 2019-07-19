from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import *
import random
from django.core.paginator import Paginator, Page
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse, request, response, JsonResponse
from django.contrib.auth import login as lgi, logout as lgo, authenticate
import random, io
from PIL import Image, ImageDraw, ImageFont

# Create your views here.
def checklogin(fun):
    def check(request, *args):
        if request.user and request.user.is_authenticated:
            return fun(request, *args)
        else:
            return redirect(reverse('goods:login'))
    return check



@checklogin
def index(request):
    first = GoodsInfo.objects.first().id
    last = GoodsInfo.objects.last().id
    d = random.randint(first, last)
    left = GoodsInfo.objects.get(pk = d)

    # print(b)
    # print(c)
    b = GoodsInfo.objects.count()
    a = random.randint(1,b-6)
    c = a+6
    # print(a)
    goods = GoodsInfo.objects.all()[a:c]
    e = a+3
    top3 = GoodsInfo.objects.all()[a:e]

    return render(request, 'lagou/index.html', locals())


@checklogin
def consult(request):
    article = Article.objects.all()
    pagenum = request.GET.get('page')
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(article, 2).get_page(pagenum)
    return render(request, 'lagou/consult.html', locals())


@checklogin
def hot(request):
    goods = GoodsInfo.objects.all()
    pagenum = request.GET.get('page')
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(goods, 2).get_page(pagenum)
    return render(request, 'lagou/hot.html', locals())


@checklogin
def orange(request, id):
    # print(type(id))
    good = GoodsInfo.objects.get(pk = id)

    id1 = str(int(id)+1)
    id2 = str(int(id)-1)
    if request.method == 'POST':
        text = request.POST.get('comment')
        user = UserInfo.objects.filter(username=request.user).first()
        c = comment()
        c.content = text
        c.star = 0
        c.user = UserInfo.objects.get(pk = user.id)
        c.goods = GoodsInfo.objects.get(pk = id)
        c.save()
        return redirect(reverse('goods:orange', args=(id,)))
        # return render(request, 'lagou/orange.html', locals())
    if request.method == 'GET':
        allcomment = good.comment_set.all()
        return render(request, 'lagou/orange.html', locals())


@checklogin
def produ(request):
    goods = GoodsInfo.objects.all()

    pagenum = request.GET.get('page')
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(goods, 2).get_page(pagenum)


    return render(request, 'lagou/produ.html',{'page':page})

def touch(request):
    return render(request, 'lagou/touch.html', {})

def base(request):
    return render(request, 'lagou/base.html', {})

def content(request, id):
    article = Article.objects.get(pk = id)
    lastid = Article.objects.last().id
    nextid = str(int(id)+1)
    if int(nextid) > int(lastid):
        return render(request, 'lagou/content.html', {'article': article, 'nextarticle': '这是最后一篇', 'nextid': id})
    nextarticle = Article.objects.get(pk = nextid).atitle


    return render(request, 'lagou/content.html',locals())


def typetag(request, id):
    type = TypeInfo.objects.get(pk = id)
    goods = type.goodsinfo_set.all()

    pagenum = request.GET.get('page')
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(goods, 2).get_page(pagenum)
    return render(request, 'lagou/produ.html', {'page':page})

def register(request):
    if request.method == 'POST':
        name = request.POST.get('user')
        password = request.POST.get('password')
        print(name,password)
        try:
            user = UserInfo.objects.create_user(username=name, password=password)
            user.is_active = False
            user.save()
        except:
            user = None

        if user:
            email = request.POST.get('email')
            recvlist = [email]
            try:
                msg = EmailMultiAlternatives("激活邮件", "<p><a href='http://127.0.0.1:8000/goods/active/%s'>点击</a></p>"%(user.id),
                                                settings.EMAIL_HOST_USER,recvlist)
                msg.content_subtype = 'html'
                msg.send()
            except Exception as a:
                print(a)
            return redirect(reverse('goods:login'))
        else:
            return render(request, 'lagou/register.html', {'errors':'注册失败'})

    return render(request, 'lagou/register.html',{})

def active(request, id):
    user = get_object_or_404(UserInfo, pk=id)
    user.is_active = True
    user.save()
    return redirect(reverse('goods:login'))



def login(request):
    if request.method == 'GET':

        return render(request, 'lagou/login.html')
    elif request.method == 'POST':
        # response = redirect(reverse('goods:indexes'))
        # response.set_cookie('name', request.POST.get('name'))
        # return response
        # request.session['name'] = request.POST.get('name')
        name = request.POST.get('user')
        password = request.POST.get('password')
        veritycode = request.POST.get('verity')
        # a = cache.get('verity')
        # print(veritycode)
        # print(a)
        if not veritycode == cache.get('verity'):
            return HttpResponse("验证码错误")
        user = authenticate(request, username=name, password=password)
        # print(user)
        # print(user.is_active)
        if user:
            if user.is_active:
                lgi(request, user)
                return redirect(reverse('goods:index'))
            else:
                return render(request, 'lagou/login.html', {'errors': '尚未激活'})
        else:

            return render(request, 'lagou/login.html', {'errors': '登录失败'})

    # return render(request, 'lagou/login.html',{})

def logout(request):
    lgo(request)
    return redirect(reverse('goods:login'))

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





#购物车
@checklogin
def cart(request):
    uid = request.user.id
    # print(uid)
    user = UserInfo.objects.get(pk=uid)
    carts = user.cartinfo_set.all()
    lenn = carts.count()
    return render(request,'lagou/cart2.html',locals())

#添加商品

def addcart(request,gid):
    #用户uid购买了gid商品，数量为count
    good = GoodsInfo.objects.get(pk = gid)
    user = request.user
    userid = user.id
    user2 = UserInfo.objects.get(pk = userid)


    count = request.POST.get('number')

    # print(count, type(count))
    #查询购物车是否已经有此商品，有则增加
    carts = CartInfo.objects.filter(user=user, goods=good).first()
    # print(carts)
    order = OrderInfo()
    if carts:
        carts.count = int(count)
        carts.save()
    else:
        cart = CartInfo()
        cart.goods = good
        cart.user = user2
        cart.count = int(count)
        cart.save()

    return redirect(reverse('goods:cart'))





def edit(request,cart_id,count):
    try:
        cart=CartInfo.objects.get(pk=int(cart_id))
        count1=cart.count=int(count)
        cart.save()
        data={'ok':0}
    except Exception as e:
        data={'ok':count1}
    return JsonResponse(data)


def delete(request,cart_id):
    cart = CartInfo.objects.get(pk = cart_id)
    cart.delete()
    return redirect(reverse('goods:cart'))

def pay(request):

    uid = request.user.id
    # print(uid)
    user = UserInfo.objects.get(pk=uid)
    carts = user.cartinfo_set.all()
    pay = 0
    num = 0
    order = OrderInfo()
    for i in carts:
        a = i.goods.gprice
        b = i.count
        # print(a,b)
        num += b
        pay += a*b
    # print(pay)
    order.user = user
    order.opay = pay
    order.ototal = num
    order.save()
    # orderdetail = OrderDetailInfo()
    for a in carts:
        orderdetail = OrderDetailInfo()
        orderdetail.goods = a.goods
        orderdetail.order = order
        orderdetail.num = a.count
        orderdetail.save()

    for b in carts:
        b.delete()
    # print('------------------')
    return redirect(reverse('goods:cart'))


def changenum(request, cartid):
    cart = CartInfo.objects.get(pk = cartid)
    print(cart.id)
    num = request.POST.get(cart.id)
    print(num)
    cart.count = num
    cart.save()
    return redirect(reverse('goods:cart'))