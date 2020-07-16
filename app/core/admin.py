from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'cdt', 'udt']
    list_filter = ['status', 'cdt', 'udt']


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'cdt', 'udt']
