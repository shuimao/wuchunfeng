from django.conf.urls import url
from .import views

app_name = 'poll2'

urlpatterns = [
    url(r'^index2/$', views.index2, name='index2'),
    url(r'^list2/(\d+)/$', views.list2, name='list2'),
    url(r'^detail2/(\d+)/$', views.detail2, name='detail2'),

]