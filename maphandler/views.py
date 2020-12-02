from django.shortcuts import render, redirect
from maphandler.models import RobotMap, RobotCoordinate
from maphandler.forms import UploadMapForm
from maphandler.serializers import RobotCoordinateSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

#change map by user 
def upload_map_view(request):
	context = {}
	initial_map = RobotMap(size_x=0, size_y=0)

	if request.POST:
		#form to upload new map
		form = UploadMapForm(request.POST, request.FILES, instance=initial_map)
		if form.is_valid():
			#save the form to Map model objext
			latest_map = form.save(commit=False)
			map_img = form.cleaned_data['map_image']
			#set the size of the uploaded map
			latest_map.size_x = map_img.image.width
			latest_map.size_y = map_img.image.height
			#set the uploader of the map
			latest_map.uploader = request.user
			#log
			print(latest_map)
			latest_map.save() 
			return redirect('home')
		else:
			#if not valid, draw current available map image instead
			latest_map = RobotMap.objects.order_by('date_updated').last()
			context['upload_map_form'] = form
	else:
		latest_map = RobotMap.objects.order_by('date_updated').last()
		form = UploadMapForm()
		context['upload_map_form'] = form

	context['map'] = latest_map
	#add form as a context to display form label
	context['map_form'] = form
	return render(request, 'maphandler/upload_map.html', context)

@api_view(['POST'])
def upload_coordinate(request):
	"""
	Upload robot coordinat to the latest uploaded map
	"""
	latest_map = RobotMap.objects.last()

	coord = RobotCoordinate(map_image=latest_map)

	if 'POST' in request.method:
		serializer = RobotCoordinateSerializer(data=request.data, instance=coord)
		if serializer.is_valid():
			print(serializer.validated_data)
			print('serializer is valid')
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		else :
			print('serializer is not valid')
		return JsonResponse(serializer.data, status=400)
	else:
		print('method is not post')

	return HttpResponse(status=404)

@api_view(['GET'])
def get_latest_position(request):
	"""
	get latest robot coordinat
	"""
	latest_pos = RobotCoordinate.objects.last()
	serializer = RobotCoordinateSerializer(latest_pos)
	return Response(serializer.data, status=status.HTTP_200_OK)




