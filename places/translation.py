from modeltranslation.translator import register, TranslationOptions

from .models import Beach, BeachImg, Landscape, LandscapeImg, Trail, TrailImg, City, Country
from .models import Cottage, CottageImg, Hospital, HospitalImg, Hotel, HotelImg, Police, PoliceImg 
from .models import RentCar, RentCarImg, Restaurant, RestaurantImg

@register(Beach)
class BeachTranslationOptions(TranslationOptions):
	fields = ('subtitle', 'description',)

@register(Landscape)
class LandscapeTranslationOptions(TranslationOptions):
	fields = ('subtitle', 'description',)

@register(Trail)
class TrailTranslationOptions(TranslationOptions):
	fields = ('subtitle', 'description',)

@register(City)
class CityTranslationOptions(TranslationOptions):
	fields = ('subtitle', 'description',)

@register(Cottage)
class CottageTranslationOptions(TranslationOptions):
	fields = ('subtitle', 'description',)

@register(Hospital)
class HospitalTranslationOptions(TranslationOptions):
	fields = ('subtitle', 'description',)

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
	fields = ('subtitle', 'description',)

@register(Police)
class PoliceTranslationOptions(TranslationOptions):
	fields = ('subtitle', 'description',)

@register(RentCar)
class RentCarTranslationOptions(TranslationOptions):
	fields = ('subtitle', 'description',)

@register(Restaurant)
class RestaurantTranslationOptions(TranslationOptions):
	fields = ('subtitle', 'description',)