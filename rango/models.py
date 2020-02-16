from django.db import models
<<<<<<< HEAD
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs): 
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
	
	class Meta: 
		verbose_name_plural = 'Categories'
	
	def __str__(self):
		return self.name 
		
class Page(models.Model): 
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=128)
	url = models.URLField() 
	views = models.IntegerField(default=0)
	
	def __str__(self): 
		return self.title 

=======

# Create your models here.
>>>>>>> 869b45a7fc1118c6dc3f3dce56330b98b589af3f
