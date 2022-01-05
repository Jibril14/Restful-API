from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Product
		fields = [
			'name',
			'description',
			'price',
			'discount' # a method define in model
		]


	def get_anything(self, obj):
		print(obj.id)  # get anything from the model instance