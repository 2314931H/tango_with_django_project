from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('about/', views.about, name='about'), 
	path('category/<slug:category_name_slug>/', 
		 views.show_category, name='show_category'),
=======
    path('about/', views.about, name='about'),
>>>>>>> 869b45a7fc1118c6dc3f3dce56330b98b589af3f
    ]
