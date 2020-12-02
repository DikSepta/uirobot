from maphandler import views
from django.urls import path

urlpatterns = [
	path('get-position/',views.get_latest_position, name='get_position'),
    path('upload-coordinate/', views.upload_coordinate, name='upload_coordinate'),
]

