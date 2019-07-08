from django.shortcuts import render, reverse, redirect
from django.conf.urls import url
from django.http import HttpResponse
from django.template import loader
from .models import *
# Create your views here.


def index2(request):
    temp = loader.get_template('poll2/index2.html')
    quet = Questions.objects.all()
    result = temp.render({'quet':quet})
    return HttpResponse(result)

def list2(request, id):
    temp = loader.get_template('poll2/list2.html')
    quet = Questions.objects.get(pk=id)
    result = temp.render({'quet':quet})
    return HttpResponse(result)

def detail2(request, id):
    quet = Questions.objects.get(pk=id)
    if request.method == "GET":
        temp = loader.get_template('poll2/detail2.html')
        result = temp.render({ 'quet':quet })
        return HttpResponse(result)
    elif request.method == "POST":
        oid = request.POST.get('option')
        opt = Options.objects.get(pk=oid)
        opt.num +=1
        opt.save()
        return redirect(reverse("poll2:detail2", args=(id,)))



