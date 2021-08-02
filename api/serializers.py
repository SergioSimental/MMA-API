from rest_framework import serializers
from rest_framework import viewsets
from .models import Fighter


class FighterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fighter
		fields = '__all__'

class FighterViewSet(viewsets.ModelViewSet):
	serializer_class = FighterSerializer
	queryset = Fighter.objects.all()