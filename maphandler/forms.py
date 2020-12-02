from django.forms import ModelForm
from django import forms
from maphandler.models import RobotMap 
from PIL import Image

class UploadMapForm(ModelForm):
	class Meta:
		model = RobotMap
		exclude = ['date_uploaded', 'date_updated', 'uploader', 'size_x', 'size_y']

	def clean(self):
		if self.is_valid():
			img = self.cleaned_data['map_image']
			print(img)
			img_format = img.image.format
			print(img_format)
			if img_format != 'PNG' and img_format != 'PGM':
				raise forms.ValidationError('choosen file is not PNG or PGM image')

