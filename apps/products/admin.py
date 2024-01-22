from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

admin.sites.AdminSite.site_header = 'پنل مدیریت جنگو'

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at', 'updated_at', 'deleted_at')
    ordering = ('id',)
    list_filter = (('created_at', JDateFieldListFilter), ('updated_at', JDateFieldListFilter), ('deleted_at', JDateFieldListFilter))
    search_fields = ('category_name', )
    list_display_links = ('category_name', )
