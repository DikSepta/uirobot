from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.
def upload_location(instance, filename = None):
	date = timezone.now()
	return	'map/{current_date}'.format(current_date=str(date))	

class RobotMap(models.Model):
	map_image = models.ImageField(upload_to=upload_location,help_text='only accept PNG or PGM image file')
	date_uploaded = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	uploader = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField(max_length=100)
	size_x = models.FloatField(blank=True, default=0, help_text='map horizontal size in pixel')
	size_y = models.FloatField(blank=True, default=0, help_text='map vertical size in pixel')
	scale_x = models.FloatField(default=0, help_text='map horizontal scale in 1 pixel : xx meter')
	scale_y = models.FloatField(default=0, help_text='map vertical scale in 1 pixel : xx meter')

	class Meta:
		ordering = ['date_updated']

	def __str__(self):
		return self.description

class RobotCoordinate(models.Model):
	map_image = models.ForeignKey(RobotMap, on_delete=models.CASCADE)
	date_uploaded = models.DateTimeField(auto_now_add=True)
	position_x = models.FloatField(default=0)
	position_y = models.FloatField(default=0)

	class Meta:
		ordering = ['date_uploaded']

	def __str__(self):
		return '({x},{y})'.format(x=self.position_x,y=self.position_y)