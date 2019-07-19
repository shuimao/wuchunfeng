from django.conf.urls import url
from . import views


app_name = 'goods'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^consult/$', views.consult, name='consult'),
    url(r'^hot/$', views.hot, name='hot'),
    url(r'^orange/(\d+)/$', views.orange, name='orange'),
    url(r'^produ/$', views.produ, name='produ'),
    url(r'^touch/$', views.touch, name='touch'),
    url(r'^base/$', views.base, name='base'),
    url(r'^content/(\d+)/$', views.content, name='content'),
    url(r'^typetag/(\d+)/$', views.typetag, name='typetag'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^active/(\d+)/$', views.active, name='active'),
    url(r'^verity/$', views.verity, name='verity'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^addcart/(\d+)/$', views.addcart, name='addcart'),
    url(r'^delete/(\d+)/$', views.delete, name='delete'),
    url(r'^pay/$', views.pay, name='pay'),
    url(r'^changenum/(\d+)/$', views.changenum, name='changenum'),
]