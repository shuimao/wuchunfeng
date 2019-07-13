from django.contrib.syndication.views import Feed
from django.shortcuts import reverse
from .models import *
class ArticleFeed(Feed):
    title = '测试博客'
    description = '介绍一些开发知识'
    link = '/blog/indexes/'

    def item(self):
        return Article.objects.order_by("-create_time")[:3]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return reverse("blog:single", args=(item.id, ))

    def item_description(self, item):
        return item.author.username + ":" + item.title