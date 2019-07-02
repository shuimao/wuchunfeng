from django.contrib import admin
from .models import *

# Register your models here.

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
#     关联个数
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
    inlines = [HeroInfoInline]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ('heroname','explain')
    list_filter = ['heroname']
    search_fields = ['heroname',]
    list_per_page = 2




admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)