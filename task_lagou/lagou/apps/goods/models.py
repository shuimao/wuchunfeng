from django.db import models
from tinymce.models import HTMLField
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import User
# Create your models here.



# 用户
class UserInfo(User):
    # uaccount = models.CharField(max_length=20)
    # pwd = models.CharField(max_length=40)
    # name = models.CharField(max_length=20)
    # email = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=20)





# 商品分类
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    # isDelete = models.BooleanField(default=False)
    def __str__(self):

        return self.ttitle

# 商品
class GoodsInfo(models.Model):
    gtype = models.ForeignKey(TypeInfo, on_delete=models.CASCADE)
    gtitle = models.CharField(max_length=20)
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    collect = models.IntegerField(default=0)
    content = models.ImageField(upload_to='goods')
    content2 = models.CharField(max_length=300 , default='')
    def __str__(self):
        return self.gtitle


class comment(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, null=True)
    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    star = models.IntegerField(default=5)

class Oreder(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)

class OrderInfo(models.Model):
    # oid = models.IntegerField(default=0)
    otime = models.DateTimeField(auto_now=True)
    opay = models.DecimalField(max_digits=5, decimal_places=2)
    ototal = models.DecimalField(max_digits=5, decimal_places=2)
    # oaddress = models.CharField(max_length=200, default='')
    # zhifu = models.IntegerField(default=0)
    user = models.ForeignKey(UserInfo , on_delete=models.CASCADE)

class OrderDetailInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE)
    # user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    # total = models.DecimalField(max_digits=6, decimal_places=2)
    num = models.IntegerField(default=0)


class Article(models.Model):
    atitle = models.CharField(max_length=50, verbose_name='名称')
    body = UEditorField(imagePath='article')
    create_time = models.DateTimeField(auto_now=True)


class CartInfo(models.Model):
    user=models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    goods=models.ForeignKey(GoodsInfo, on_delete=models.CASCADE)
    count=models.IntegerField(default=0)