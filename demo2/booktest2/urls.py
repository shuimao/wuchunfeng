from django.conf.urls import url
from . import views

app_name = 'booktest2'

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^roledel/(\d+)/$', views.roledel, name='roledel'),
    url(r'^roleadd/(\d+)/$', views.roleadd, name='roleadd'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^verity/$', views.verity, name='verity'),
    url(r'^active/(\d+)/$', views.active, name='active')
]