from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^list/(\d+)/$',views.list),
    url(r'^detail/(\d+)/$', views.detail),

]
