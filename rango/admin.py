from django.contrib import admin
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> d4de8fe961fdb9096503bdabff8282bd4afbf255
from rango.models import Category, Page 

class CategoryAdmin(admin.ModelAdmin): 
	prepopulated_fields = {'slug': ('name',)}

class PageAdmin(admin.ModelAdmin): 
	list_display = ('title', 'category', 'url')

# Register your models here.

admin.site.register(Category, CategoryAdmin)
<<<<<<< HEAD
admin.site.register(Page, PageAdmin)
=======
admin.site.register(Page, PageAdmin)
=======

# Register your models here.
>>>>>>> e777434e43069fb9fea6c4bb2b154dcc15c41f1a
>>>>>>> d4de8fe961fdb9096503bdabff8282bd4afbf255
