from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import loader
from django.core import serializers

from .models import Beach, BeachImg, Landscape, LandscapeImg, Trail, TrailImg, City, Country
import json

# Create your views here.

from django.shortcuts import (
	render_to_response
)
from django.template import RequestContext

# HTTP Error 400
def bad_request(request):
	response = render_to_response(
		'404.html',
		context_instance=RequestContext(request)
	)
	response.status_code = 400
	return response

#HTTP Error 404
def page_not_found(request):
	response = render_to_response(
		'404.html',
		context_instance=RequestContext(request)
	)
	response.status_code = 404
	return response

def server_error(request):
	response = render_to_response(
		'404.html',
		context_instance=RequestContext(request)
	)
	response.status_code = 500
	return response

def start(request):
	return render(request, 'index.html')


#def index(request):
#	return render(request, 'start.html')

#def home(request):
#	return render(request, 'index.html')


#def start(request):
#	return render(request, 'start.html')


def home_beach(request):
	if request.method == 'GET':
		pais = Country.objects.filter(name = 'Chile')
		ciudad_pais = City.objects.filter(country = pais).filter(name = 'Ancud')
		playas = Beach.objects.filter(city = ciudad_pais)
		context = {
			'playas': playas,
		}
		template = loader.get_template('home_beachs.html')
		return HttpResponse(template.render(context, request))



def home_trails(request):
	if request.method == 'GET':
		pais = Country.objects.filter(name = 'Chile')
		ciudad_pais = City.objects.filter(country = pais).filter(name = 'Ancud')
		trail = Trail.objects.filter(city = ciudad_pais)
		context = {
			'senderos': trail,
		}
		template = loader.get_template('home_trails.html')
		return HttpResponse(template.render(context, request))



def home_landscapes(request):
	pais = Country.objects.filter(name = 'Chile')
	ciudad_pais = City.objects.filter(country = pais).filter(name='Ancud')
	landscape = Landscape.objects.filter(city = ciudad_pais)
	context = {
		'paisajes': landscape,
	}
	template = loader.get_template('home_landscapes.html')
	return HttpResponse(template.render(context, request))

def home_map_city(request):
	pais = Country.objects.filter(name = 'Chile')
	ciudad_pais = City.objects.filter(country = pais).filter(name = 'Ancud')
	context = {
		'ciudad_pais': ciudad_pais,
	}
	template = loader.get_template('home_map_city.html')
	return HttpResponse(template.render(context, request))


def get_locations(request):
	pais = Country.objects.filter(name = 'Chile')
	ciudad_pais = City.objects.filter(country = pais).filter(name = 'Ancud')
	landscape = Landscape.objects.filter(city = ciudad_pais)
	#array_land = []
	img_lands = LandscapeImg.objects.all()
	data = serializers.serialize('json', img_lands)

	return HttpResponse(data, content_type="application/json")
