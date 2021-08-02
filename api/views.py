from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Fighter
from .serializers import FighterSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins


# Create your views here.

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
			mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
			mixins.DestroyModelMixin):
	
	serializer_class = FighterSerializer
	queryset = Fighter.objects.all()

	lookup_field = 'id'

	def get(self, request, id=None):
		if id:
			return self.retrieve(request)
		else:
			return self.list(request)


	def post(self, request):
		return self.create(request)

	def put(self,request, id= None):
		return self.update(request, id)

	def delete(self,request,id):
		return self.delete(request,id)


class FighterAPIView(APIView):
	
	def get(self, request):
		fighters = Fighter.objects.all()
		serializer = FighterSerializer(fighters, many = True)
		return Response(serializer.data)

	def post(self, request):
		serializer = FighterSerializer(data = request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status= status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class FighterDetailAPIView(APIView):
	
	def get_object(self, id):
		try:
			return Fighter.objects.get(id=id)

		except  Fighter.DoesNotExist:
			return HttpResponse(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, id):
		fighter = self.get_object(id)
		serializer = FighterSerializer(fighter)
		return Response(serializer.data)

	def put(self, request, id):
		fighter = self.get_object(id)
		serializer = FighterSerializer(fighter, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id):
		fighter = self.get_object(id)
		fighter.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def fighter_list(request):
	if request.method == 'GET':
		fighters = Fighter.objects.all()
		serializer = FighterSerializer(fighters, many = True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = FighterSerializer(data = request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status= status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE' ])
def fighter_detail(request, pk):
	try:
		fighter = Fighter.objects.get(pk=pk)

	except  Fighter.DoesNotExist:
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)
	
	if request.method == 'GET':
		serializer = FighterSerializer(fighter)
		return Response(serializer.data)
	
	elif request.method == 'PUT':
		serializer = FighterSerializer(fighter, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif  request.method == 'DELETE':
		fighter.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

