from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    list_filter = ('category', 'title')
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'visits', 'likes')
    
admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)