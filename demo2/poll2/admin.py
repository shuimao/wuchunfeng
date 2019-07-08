from django.contrib import admin
from .models import *
# Register your models here

class OptionInline(admin.StackedInline):
    model = Options
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


admin.site.register(Questions, QuestionAdmin)
admin.site.register(Options)