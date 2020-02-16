from django.contrib import admin
<<<<<<< HEAD
from rango.models import Category, Page 

class CategoryAdmin(admin.ModelAdmin): 
	prepopulated_fields = {'slug': ('name',)}

class PageAdmin(admin.ModelAdmin): 
	list_display = ('title', 'category', 'url')

# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
=======

# Register your models here.
>>>>>>> 869b45a7fc1118c6dc3f3dce56330b98b589af3f
