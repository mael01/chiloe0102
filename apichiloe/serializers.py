from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from places.models import Beach, BeachImg, Landscape, LandscapeImg, Trail, TrailImg, City, Country
from places.models import Cottage, CottageImg, Hospital, HospitalImg, Hotel, HotelImg, Police, PoliceImg 
from places.models import RentCar, RentCarImg, Restaurant, RestaurantImg


class ImgRestaurantSerializer(ModelSerializer):
	class Meta:
		model = RestaurantImg
		field = fields = ['id', 'description', 'image']

class RestaurantSerializer(ModelSerializer):
	img_place = ImgRestaurantSerializer(many = True)

	class Meta:
		model = Restaurant
		fields = ['id', 'name', 'subtitle', 'description', 'latitude', 'longitue', 'img_refer','img_place']

class ImgRentCarSerializer(ModelSerializer):
	class Meta:
		model = RentCarImg
		fields = ['id', 'description', 'image']

class RentCarSerializer(ModelSerializer):
	img_place = ImgRentCarSerializer(many = True)

	class Meta:
		model = RentCar
		fields = ['id', 'name', 'subtitle', 'description', 'latitude', 'longitue', 'img_refer','img_place']

class ImgPoliceSerializer(ModelSerializer):
	class Meta:
		model = PoliceImg
		fields = ['id', 'description', 'image']

class PoliceSerializer(ModelSerializer):
	img_place = ImgPoliceSerializer(many = True)
	
	class Meta:
		model = Police
		fields = ['id', 'name', 'subtitle', 'description', 'latitude', 'longitue', 'img_refer','img_place']

class ImgHotelSerializer(ModelSerializer):
	class Meta:
		model = HotelImg
		fields = ['id', 'description', 'image']

class HotelSerializer(ModelSerializer):
	img_place = ImgHotelSerializer(many = True)

	class Meta:
		model = Hotel
		fields = ['id', 'name', 'subtitle', 'description', 'latitude', 'longitue', 'img_refer', 'img_place']

class ImgHospitalSerializer(ModelSerializer):
	class Meta: 
		model = HospitalImg
		fields = ['id', 'description', 'image']

class HospitalSerializer(ModelSerializer):
	img_place = ImgHospitalSerializer(many = True)

	class Meta:
		model = Hospital
		fields = ['id', 'name', 'subtitle', 'description', 'latitude', 'longitue', 'img_refer', 'img_place']

class ImgCottageSerializer(ModelSerializer):
	class Meta:
		model = CottageImg
		fields = ['id', 'description', 'image']

class CottageSerializer(ModelSerializer):
	img_place = ImgCottageSerializer(many = True)

	class Meta:
		model = Cottage
		fields = ['id', 'name', 'subtitle', 'description', 'latitude', 'longitue', 'img_refer', 'img_place']


class ImgBeachSerializer(ModelSerializer):
	class Meta:
		model = BeachImg
		fields = ['id', 'description', 'image']

class BeachSerializer(ModelSerializer):
	img_place = ImgBeachSerializer(many = True)

	class Meta:
		model = Beach
		fields = ['id', 'name', 'subtitle', 'description', 'latitude', 'longitue', 'img_refer', 'img_place']

class ImgLandSerializer(ModelSerializer):
	class Meta:
		model = LandscapeImg
		fields = ['id', 'description', 'image']

class LandSerializer(ModelSerializer):
	img_place = ImgLandSerializer(many = True)

	class Meta:
		model = Landscape
		fields = ['id', 'name', 'subtitle', 'description', 'latitude', 'longitue', 'img_refer', 'img_place']

class ImgTrailSerializer(ModelSerializer):
	class Meta:
		model = TrailImg
		fields = ['id', 'description', 'image']

class TrailSerializer(ModelSerializer):
	#Esta variable debe tener el mismo nombre que el related_name que definan en el modelo
	img_place = ImgTrailSerializer(many = True)

	class Meta:
		model = Trail
		#img_place es el nombre del related_name del modelo
		fields = ['id', 'name', 'subtitle', 'description', 'latitude', 'longitue', 'img_refer', 'img_place']

class CitySerializer(ModelSerializer):
	beachs = BeachSerializer(many = True)
	landscapes = LandSerializer(many = True)
	trails = TrailSerializer(many = True)
	cottages = CottageSerializer(many = True)
	hospitals = HospitalSerializer(many = True)
	hotels = HotelSerializer(many = True)
	polices = PoliceSerializer(many = True)
	rentcars = RentCarSerializer(many = True)
	restaurants = RestaurantSerializer(many = True)

	class Meta:
		model = City
		fields = ['id', 'name', 'beachs', 'landscapes', 'trails', 'cottages', 'hospitals', 'hotels', 'polices', 'rentcars', 'restaurants']


