from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    # url(r'^indexes/$',views.indexes, name='indexes'),
    url(r'^indexes/$', views.ListView.as_view(), name="indexes"),
    url(r'^list/(\d+)/$',views.list, name='list'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^deletehero/(\d+)/$', views.deletehero, name='deletehero'),
    url(r'^addhero/(\d+)/$',views.addhero, name='addhero'),
    url(r'^addbook/$', views.addbook, name='addbook'),

]
