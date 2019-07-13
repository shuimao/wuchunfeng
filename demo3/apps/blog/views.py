from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from comment.models import *
from django.views.generic import View
from .forms import ArticleForm, CommentForm
from django.core.paginator import Paginator, Page
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.




def getpage(request, object_list, num):
    pagenum = request.GET.get("page")
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(object_list, num).get_page(pagenum)
    return page

@cache_page(timeout=120)
def index(request):

    value = cache.get("111")
    print(value)
    cache.set('111', 'task')
    value = cache.get('111')
    print(value)

    ads = Ads.objects.all()
    articles = Article.objects.all()
    page = getpage(request, articles, 1)
    return render(request, 'blog/index.html', {"page": page, "ads":ads})





class IndexView(View):
    def get(self, request):
        ads = Ads.objects.all()
        articles = Article.objects.all()
        page = getpage(request, articles, 1)
        # pagenum = request.GET.get("page")
        # pagenum = 1 if not pagenum else pagenum
        # page = Paginator(articles,1).get_page(pagenum)
        # paginator = Paginator(articles, 1)
        return render(request, 'blog/index.html', {"page":page, "ads":ads})


class SingleView(View):
    def get(self, request, id):
        # article = Article.objects.all()
        article = get_object_or_404(Article, pk=id)
        article.views += 1
        article.save()
        cmf = CommentForm()
        return render(request, 'blog/single.html', {'article':article, "cmf":cmf})
    def post(self, request, id):
        article = get_object_or_404(Article, pk=id)
        cmf = CommentForm(request.POST)
        comm = cmf.save(commit=False)
        comm.article = article
        comm.save()
        # return render(request, 'blog/single.html')   ???
        return redirect(reverse('blog:single',args=(article.id, )))

class AddArticleView(View):
    def get(self,request):
        af = ArticleForm()
        return render(request, 'blog/addarticle.html', locals())
    def post(self, request):
        af = ArticleForm(request.POST)
        if af.is_valid():
            article = af.save(commit=False)
            article.category = Category.objects.first()
            article.author = User.objects.first()
            article.save()
            return redirect(reverse('blog:index'))

        return HttpResponse('添加成功')


class Getarticles(View):
    def get(self, request, year, month):
        article = Article.objects.filter(create_time__year = year, create_time__month = month)
        page = getpage(request, article, 1)
        return render(request, 'blog/index.html', {'page':page})


class Articlecategory(View):
    def get(self, request, id):
        category = Category.objects.get(pk = id)
        articles = category.article_set.all()
        page = getpage(request, articles, 1)
        return render(request, 'blog/index.html', {'page':page})

class Tagacticle(View):
    def get(self, request, id):
        tag = Tag.objects.get(pk=id)
        articles = tag.article_set.all()
        page = getpage(request, articles, 1)
        return render(request, 'blog/index.html', {'page': page})

class AddComment(View):
    def post(self, request, id):
        name = request.POST.get('name')
        email = request.POST.get('email')
        url = request.POST.get('url')
        content = request.POST.get('content')
        c = Comment()
        c.name = name
        c.email = email
        c.url = url
        c.content = content
        c.article = Article.objects.get(pk=id)
        c.save()
        return JsonResponse({'name':c.name, 'url':c.url, 'email':c.email, 'content':c.content, 'create_time':c.create_time})