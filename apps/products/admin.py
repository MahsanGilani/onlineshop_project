from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at', 'updated_at', 'deleted_at')
    ordering = ('id',)
    list_filter = ('created_at', 'updated_at', 'deleted_at')
    search_fields = ('category_name', )
    list_display_links = ('category_name', )
