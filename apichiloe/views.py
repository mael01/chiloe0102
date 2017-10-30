from django.shortcuts import render, get_list_or_404, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from places.models import Beach, BeachImg, Landscape, LandscapeImg, Trail, TrailImg, City, Country
from .serializers import CitySerializer

# Create your views here.
class HolaMundo(APIView):
	def get(self, request, format = None):
		return Response({'Mensaje': 'Hola Mundo'})

hola = HolaMundo.as_view()


class Citys(APIView):

	serializer_class = CitySerializer

	def get(self, request, id = None, format = None):
		if id != None:
			ciudades = get_object_or_404(City, pk = id)
			many = False
		else:
			ciudades = City.objects.all()
			many = True

		response = self.serializer_class(ciudades, many = many, read_only=True)
		return Response(response.data)

citys = Citys.as_view()