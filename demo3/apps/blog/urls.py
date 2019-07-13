from django.conf.urls import url
from . import views
from .feeds import ArticleFeed

app_name = "blog"

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    # url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^single/(\d+)/$', views.SingleView.as_view(), name='single'),
    url(r'^addarticle/$', views.AddArticleView.as_view(), name='addarticle'),
    url(r'^getarticles/(\d+)/(\d+)/$', views.Getarticles.as_view(), name='getarticles'),
    url(r'^articlecategory/(\d+)/$', views.Articlecategory.as_view(), name='articlecategory'),
    url(r'^tagacticle/(\d+)/$', views.Tagacticle.as_view(), name='tagacticle'),
    url(r'^rss/$', ArticleFeed()),
    url(r'^comment/(\d+)/$', views.AddComment.as_view(), name='comment')
]