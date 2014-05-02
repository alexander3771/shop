from django.contrib import admin
from models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'published', 'ordering', 'pic')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(ProductImages)
