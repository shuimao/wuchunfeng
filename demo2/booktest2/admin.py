from django.contrib import admin
from .models import *
# Register your models here.

class RoleInline(admin.StackedInline):
    model = role
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [RoleInline]


admin.site.register(Books, BookAdmin)
admin.site.register(role)
