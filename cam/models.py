from django.db import models

# Create your models here.
class Image(models.Model):
	image_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.image_name

class Photo(models.Model):
	names= models.CharField(max_length=200)