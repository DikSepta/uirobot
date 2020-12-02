from django.shortcuts import render
from maphandler.models import RobotMap

def home_view(response):
	context = {}
	latest_map = RobotMap.objects.order_by('date_updated').last()

	context['map'] = latest_map
	print(latest_map.map_image.url);
	return render(response,"base.html", context) 