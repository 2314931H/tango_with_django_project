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
>>>>>>> e777434e43069fb9fea6c4bb2b154dcc15c41f1a
