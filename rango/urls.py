from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> d4de8fe961fdb9096503bdabff8282bd4afbf255
    path('about/', views.about, name='about'), 
	path('category/<slug:category_name_slug>/', 
		views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'), 
	path('category/<slug:category_name_slug>/add_page/', 
		views.add_page, name='add_page'), 
	]
<<<<<<< HEAD
=======
=======
    path('about/', views.about, name='about'),
    ]
>>>>>>> e777434e43069fb9fea6c4bb2b154dcc15c41f1a
>>>>>>> d4de8fe961fdb9096503bdabff8282bd4afbf255
