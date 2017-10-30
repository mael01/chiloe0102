from django.contrib import admin

# Register your models here.
from .models import Beach, BeachImg, Landscape, LandscapeImg, Trail, TrailImg, City, Country
from .models import Cottage, CottageImg, Hospital, HospitalImg, Hotel, HotelImg, Police, PoliceImg 
from .models import RentCar, RentCarImg, Restaurant, RestaurantImg


class RestaurantInLine(admin.TabularInline):
	model = Restaurant
	extra = 0

class RestaurantImgInLine(admin.TabularInline):
	model = RestaurantImg
	extra = 0

class RentCarInLine(admin.TabularInline):
	model = RentCar
	extra = 0

class RentCarImgInLine(admin.TabularInline):
	model = RentCarImg
	extra = 0

class PoliceInLine(admin.TabularInline):
	model = Police
	extra = 0

class PoliceImgInLine(admin.TabularInline):
	model = PoliceImg
	extra = 0

class HotelInLine(admin.TabularInline):
	model = Hotel
	extra = 0

class HotelImgInLine(admin.TabularInline):
	model = HotelImg
	extra = 0

class HospitalInLine(admin.TabularInline):
	model = Hospital
	extra = 0

class HospitalImgInLine(admin.TabularInline):
	model = HospitalImg
	extra = 0

class CityInLine(admin.TabularInline):
	model = City
	extra = 0

class CountryInLine(admin.TabularInline):
	model = Country
	extra = 0

class BeachInLine(admin.TabularInline):
	model = Beach
	extra = 0

class BeachImgInLine(admin.TabularInline):
	model = BeachImg
	extra = 0

class CottageInLine(admin.TabularInline):
	model = Cottage
	extra = 0

class CottageImgInLine(admin.TabularInline):
	model = CottageImg
	extra = 0

class LandscapeInLine(admin.TabularInline):
	model = Landscape
	extra = 0

class LandscapeImgInLine(admin.TabularInline):
	model = LandscapeImg
	extra = 0

class TrailInLine(admin.TabularInline):
	model = Trail
	extra = 0

class TrailImgInLine(admin.TabularInline):
	model = TrailImg
	extra = 0



class RestaurantAdmin(admin.ModelAdmin):
	list_display = ['name', 'subtitle', 'description']
	inlines = [RestaurantImgInLine]
	search_fields = ('name',)

class RestaurantImgAdmin(admin.ModelAdmin):
	search_fields = ('restaurant__name',)

class RentCarAdmin(admin.ModelAdmin):
	list_display = ['name', 'subtitle', 'description']
	inlines = [RentCarImgInLine]
	search_fields = ('name',)

class RentCarImgAdmin(admin.ModelAdmin):
	search_fields = ('rentcar__name',)


class PoliceAdmin(admin.ModelAdmin):
	list_display = ['name', 'subtitle', 'description']
	inlines = [PoliceImgInLine]
	search_fields = ('name',)

class PoliceImgAdmin(admin.ModelAdmin):
	search_fields = ('police__name',)


class HotelAdmin(admin.ModelAdmin):
	list_display = ['name', 'subtitle', 'description']
	inlines = [HotelImgInLine]
	search_fields = ('name',)

class HotelImgAdmin(admin.ModelAdmin):
	search_fields = ('hotel__name',)


class CountryAdmin(admin.ModelAdmin):
	list_display = ['name']
	inlines = [CityInLine]
	search_fields = ('name',)

class CityAdmin(admin.ModelAdmin):
	list_display = ['name']
	inlines = [BeachInLine, LandscapeInLine, TrailInLine, CottageInLine, HospitalInLine, HotelInLine, PoliceInLine, RentCarInLine, RestaurantInLine]
	search_fields = ('name',)


class HospitalAdmin(admin.ModelAdmin):
	list_display = ['name', 'subtitle', 'description']
	inlines = [HospitalImgInLine]
	search_fields = ('name',)

class HospitalImgAdmin(admin.ModelAdmin):
	search_fields = ('hospital__name',)


class CottageAdmin(admin.ModelAdmin):
	list_display = ['name', 'subtitle', 'description']
	inlines = [CottageImgInLine]
	search_fields = ('name',)

class CottageImgAdmin(admin.ModelAdmin):
	search_fields = ('cottage__name',)

class BeachAdmin(admin.ModelAdmin):
	list_display = ('name', 'subtitle', 'description')
	inlines = [BeachImgInLine]
	search_fields = ('name',)

class BeachImgAdmin(admin.ModelAdmin):
	search_fields = ('beach__name',)

class LandscapeAdmin(admin.ModelAdmin):
	search_fields = ('name',)
	inlines = [LandscapeImgInLine]

class LandscapeImgAdmin(admin.ModelAdmin):
	search_fields = ('landscape__name',)

class TrailAdmin(admin.ModelAdmin):
	search_fields = ('name',)
	inlines = [TrailImgInLine]

class TrailImgAdmin(admin.ModelAdmin):
	search_fields = ('trail__name',)















admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Cottage, CottageAdmin)
admin.site.register(CottageImg, CottageImgAdmin)
admin.site.register(Beach, BeachAdmin)
admin.site.register(BeachImg, BeachImgAdmin)
admin.site.register(Landscape, LandscapeAdmin)
admin.site.register(LandscapeImg, LandscapeImgAdmin)
admin.site.register(Trail, TrailAdmin)
admin.site.register(TrailImg, TrailImgAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(HospitalImg, HospitalImgAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelImg, HotelImgAdmin)
admin.site.register(Police, PoliceAdmin)
admin.site.register(PoliceImg, PoliceImgAdmin)
admin.site.register(RentCar, RentCarAdmin)
admin.site.register(RentCarImg, RentCarImgAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(RestaurantImg, RestaurantImgAdmin)


