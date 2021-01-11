from rest_framework import serializers
from .models import image_to_json

class image_to_jsonSerializer(serializers.ModelSerializer):
	# movie_image = serializers.FileField(max_length=None, use_url=True, required=False)

	class Meta:
		"""docstring for Meta"""
		model = image_to_json
		# fields = ('name', 'age')
		fields = ('id', 'movie_image' , 'data')
			