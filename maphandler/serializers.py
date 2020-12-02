from maphandler.models import RobotCoordinate
from rest_framework import serializers

class RobotCoordinateSerializer(serializers.ModelSerializer):
	class Meta:
		model = RobotCoordinate
		fields = ['position_x', 'position_y']

	def update(self, instance, validated_data):
		#convert coordinate from meters to pixel
		instance.position_x = instance.map_image.scale_x * validated_data.get('position_x',instance.position_x)
		instance.position_y = instance.map_image.scale_y * validated_data.get('position_y',instance.position_y)
		instance.save()
		return instance