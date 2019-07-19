from django.contrib import admin
from .models import *

# Register your models here.
class GoodsInline(admin.StackedInline):
    model = GoodsInfo
    extra = 1

class TypeIline(admin.ModelAdmin):
    inlines = [GoodsInline]


admin.site.register(UserInfo)
admin.site.register(GoodsInfo)
admin.site.register(TypeInfo)
admin.site.register(Article)