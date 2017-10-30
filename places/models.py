from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import date

class Country(models.Model):
	name = models.CharField( max_length = 100, null = False, default = '')
	subtitle = models.CharField( max_length = 100, default = '' )
	description = models.CharField( max_length = 2000, null = False, default = '')
	def __str__(self):
		return '%s' % (self.name)

class City(models.Model):
	name = models.CharField( max_length = 100, null = False, default = '')
	subtitle = models.CharField( max_length = 100, default = '' )
	description = models.CharField( max_length = 2000, null = False, default = '')
	country = models.ForeignKey(Country, on_delete = models.CASCADE, blank = True, null = True)

	def __str__(self):
		return '%s' % (self.name)

class Police(models.Model):
	name = models.CharField( max_length = 255, null = False, default = '' )
	subtitle = models.CharField( max_length = 100, default = '' )
	description = models.CharField( max_length = 600, default = '' )
	img_refer = models.ImageField(upload_to = 'static/img/police', null = True )
	latitude = models.FloatField(default=0.0)
	longitue = models.FloatField(default=0.0)
	datestore = models.DateField(default = date.today)
	city = models.ForeignKey(City, related_name = 'polices', on_delete = models.CASCADE, blank = True, null = True)

	"""
	class Meta:
		unique_together = ('city',)
	"""

	def __str__(self):
		return '%s %s %s' % (self.name, self.subtitle, self. description)

class PoliceImg(models.Model):
	description = models.TextField(blank = True, default = True )
	image = models.ImageField(upload_to = 'static/img/police', null = True)
	police = models.ForeignKey(Police, related_name = 'img_place', on_delete = models.CASCADE, blank=True, null=True)
	datestore = models.DateField(default = date.today)
	"""
	class Meta:
		unique_together = ('police',)
	"""
	def __str__(self):
		return '%s %s' % (self.description, self.image)


class Hospital(models.Model):
	name = models.CharField( max_length = 255, null = False, default = '' )
	subtitle = models.CharField( max_length = 100, default = '' )
	description = models.CharField( max_length = 600, default = '' )
	img_refer = models.ImageField(upload_to = 'static/img/hospital', null = True )
	latitude = models.FloatField(default=0.0)
	longitue = models.FloatField(default=0.0)
	datestore = models.DateField(default = date.today)
	city = models.ForeignKey(City, related_name = 'hospitals', on_delete = models.CASCADE, blank = True, null = True)
	"""
	class Meta:
		unique_together = ('city',)
	"""

	def __str__(self):
		return '%s %s %s' % (self.name, self.subtitle, self. description)

class HospitalImg(models.Model):
	description = models.TextField(blank = True, default = True )
	image = models.ImageField(upload_to = 'static/img/hospital', null = True)
	hospital = models.ForeignKey(Hospital, related_name = 'img_place', on_delete = models.CASCADE, blank=True, null=True)
	datestore = models.DateField(default = date.today)
	"""
	class Meta:
		unique_together = ('hospital',)
	"""
	def __str__(self):
		return '%s %s' % (self.description, self.image)


class Cottage(models.Model):
	name = models.CharField( max_length = 255, null = False, default = '' )
	subtitle = models.CharField( max_length = 100, default = '' )
	description = models.CharField( max_length = 600, default = '' )
	img_refer = models.ImageField(upload_to = 'static/img/cottage', null = True )
	latitude = models.FloatField(default=0.0)
	longitue = models.FloatField(default=0.0)
	datestore = models.DateField(default = date.today)
	city = models.ForeignKey(City, related_name = 'cottages', on_delete = models.CASCADE, blank = True, null = True)
	"""
	class Meta:
		unique_together = ('city',)
	"""

	def __str__(self):
		return '%s %s %s' % (self.name, self.subtitle, self. description)

class CottageImg(models.Model):
	description = models.TextField(blank = True, default = True )
	image = models.ImageField(upload_to = 'static/img/cottage', null = True)
	cottage = models.ForeignKey(Cottage, related_name = 'img_place', on_delete = models.CASCADE, blank=True, null=True)
	datestore = models.DateField(default = date.today)
	"""
	class Meta:
		unique_together = ('cottage',)
	"""

	def __str__(self):
		return '%s %s' % (self.description, self.image)


class Restaurant(models.Model):
	name = models.CharField( max_length = 255, null = False, default = '' )
	subtitle = models.CharField( max_length = 100, default = '' )
	description = models.CharField( max_length = 600, default = '' )
	img_refer = models.ImageField(upload_to = 'static/img/restaurant', null = True )
	latitude = models.FloatField(default=0.0)
	longitue = models.FloatField(default=0.0)
	datestore = models.DateField(default = date.today)
	city = models.ForeignKey(City, related_name = 'restaurants', on_delete = models.CASCADE, blank = True, null = True)
	"""
	class Meta:
		unique_together = ('city',)
	"""

	def __str__(self):
		return '%s %s %s' % (self.name, self.subtitle, self. description)

class RestaurantImg(models.Model):
	description = models.TextField(blank = True, default = True )
	image = models.ImageField(upload_to = 'static/img/restaurant', null = True)
	restaurant = models.ForeignKey(Restaurant, related_name = 'img_place', on_delete = models.CASCADE, blank=True, null=True)
	datestore = models.DateField(default = date.today)
	"""
	class Meta:
		unique_together = ('restaurant',)
	"""

	def __str__(self):
		return '%s %s' % (self.description, self.image)

class Menu(models.Model):
	name = models.CharField( max_length = 255, null = False, default = '' )
	price = models.IntegerField( default = 2000 )
	description = models.CharField( max_length = 500, null = False, default = '' )
	created = models.DateField(default = date.today)
	restaurant = models.ForeignKey(Restaurant, related_name = 'menu_restaurant', on_delete = models.CASCADE, blank=True, null=True)

class Lunch(models.Model):
	name = models.CharField( max_length = 255, null = False, default = '' )
	available = models.BooleanField( default = True, null = False )
	price = models.IntegerField( default = 2000 )
	description = models.CharField( max_length = 500, null = False, default = '' )
	created = models.DateField(default = date.today)
	restaurant = models.ForeignKey(Restaurant, related_name = 'lunch_restaurant', on_delete = models.CASCADE, blank=True, null=True)


class Hotel(models.Model):
	name = models.CharField( max_length = 255, null = False, default = '' )
	subtitle = models.CharField( max_length = 100, default = '' )
	description = models.CharField( max_length = 600, default = '' )
	img_refer = models.ImageField(upload_to = 'static/img/hotel', null = True )
	latitude = models.FloatField(default=0.0)
	longitue = models.FloatField(default=0.0)
	datestore = models.DateField(default = date.today)
	city = models.ForeignKey(City, related_name = 'hotels', on_delete = models.CASCADE, blank = True, null = True)

	"""
	class Meta:
		unique_together = ('city',)
	"""

	def __str__(self):
		return '%s %s %s' % (self.name, self.subtitle, self. description)

class HotelImg(models.Model):
	description = models.TextField(blank = True, default = True )
	image = models.ImageField(upload_to = 'static/img/hotel', null = True)
	hotel = models.ForeignKey(Hotel, related_name = 'img_place', on_delete = models.CASCADE, blank=True, null=True)
	datestore = models.DateField(default = date.today)

	"""
	class Meta:
		unique_together = ('hotel',)
	"""

	def __str__(self):
		return '%s %s' % (self.description, self.image)


class RentCar(models.Model):
	name = models.CharField( max_length = 255, null = False, default = '' )
	subtitle = models.CharField( max_length = 100, default = '' )
	description = models.CharField( max_length = 600, default = '' )
	img_refer = models.ImageField(upload_to = 'static/img/rentcar', null = True )
	latitude = models.FloatField(default=0.0)
	longitue = models.FloatField(default=0.0)
	datestore = models.DateField(default = date.today)
	city = models.ForeignKey(City, related_name = 'rentcars', on_delete = models.CASCADE, blank = True, null = True)

	"""
	class Meta:
		unique_together = ('city',)
	"""

	def __str__(self):
		return '%s %s %s' % (self.name, self.subtitle, self. description)

class RentCarImg(models.Model):
	description = models.TextField(blank = True, default = True )
	image = models.ImageField(upload_to = 'static/img/rentcar', null = True)
	rentcar = models.ForeignKey(RentCar, related_name = 'img_place', on_delete = models.CASCADE, blank=True, null=True)
	datestore = models.DateField(default = date.today)

	"""
	class Meta:
		unique_together = ('rentcar',)
	"""

	def __str__(self):
		return '%s %s' % (self.description, self.image)

# Create your models here.
class Landscape(models.Model):
	name = models.CharField( max_length = 100, default = '' )
	subtitle = models.CharField( max_length = 100, default = '' )
	description = models.CharField( max_length = 600, default = '' )
	img_refer = models.ImageField(upload_to = 'static/img/landscape', null = True )
	latitude = models.FloatField(default=0.0)
	longitue = models.FloatField(default=0.0)
	datestore = models.DateField(default = date.today)
	city = models.ForeignKey(City, related_name = 'landscapes', on_delete = models.CASCADE, blank = True, null = True)
	"""
	class Meta:
		unique_together = ('city',)
	"""

	def __str__(self):
		return '%s %s %s' % (self.name, self.subtitle, self. description)

class LandscapeImg(models.Model):
	description = models.TextField(blank = True, default = True )
	image = models.ImageField(upload_to = 'static/img/landscape', null = True)
	principal = models.BooleanField(default = False)
	landscape = models.ForeignKey(Landscape, related_name = 'img_place', on_delete = models.CASCADE, blank=True, null=True)
	datestore = models.DateField(default = date.today)

	"""
	class Meta:
		unique_together = ('landscape',)
	"""

	def __str__(self):
		return '%s %s' % (self.description, self.image)

class Beach(models.Model):
	name = models.CharField( max_length = 100, null = False, default = '' )
	subtitle = models.CharField( max_length = 100, default = '' )
	description = models.CharField( max_length = 600, default = '' )
	img_refer = models.ImageField(upload_to = 'static/img/beachs', null = True )
	latitude = models.FloatField(default=0.0)
	longitue = models.FloatField(default=0.0)
	datestore = models.DateField(default = date.today)
	city = models.ForeignKey(City, related_name = 'beachs', on_delete = models.CASCADE, blank = True, null = True)
	"""
	class Meta:
		unique_together = ('city',)
	"""
	def __str__(self):
		return '%s %s %s' % (self.name, self.subtitle, self. description)

class BeachImg(models.Model):
	description = models.TextField(blank = True, default = '' )
	image = models.ImageField(upload_to = 'static/img/beachs', null = True)
	principal = models.BooleanField(default = False)
	datestore = models.DateField(default = date.today)
	beach = models.ForeignKey(Beach, related_name = 'img_place', on_delete = models.CASCADE, blank = True, null = True)

	"""
	class Meta:
		unique_together = ('beach',)
	"""

	def __str__(self):
		return '%s %s' % (self.description, self.image)

class Trail(models.Model):
	name = models.CharField( max_length = 255, default = ''  )
	subtitle = models.CharField( max_length = 255, default = ''  )
	description = models.CharField( max_length = 600, default = ''  )
	img_refer = models.ImageField(upload_to = 'static/img/trails', null = True )
	latitude = models.FloatField(default=0.0)
	longitue = models.FloatField(default=0.0)
	datestore = models.DateField(default = date.today)
	city = models.ForeignKey(City, related_name = 'trails', on_delete = models.CASCADE, blank = True, null = True)
	"""
	class Meta:
		unique_together = ('city',)
	"""

	def __str__(self):
		return '%s %s %s' % (self.name, self.subtitle, self. description)

class TrailImg(models.Model):
	description = models.TextField(blank = True, default = '' )
	image = models.ImageField(upload_to = 'static/img/trails', null = True)
	principal = models.BooleanField(default = False)
	trail = models.ForeignKey(Trail, related_name = 'img_place', on_delete = models.CASCADE, blank=True, null=True)
	datestore = models.DateField(default = date.today)
	
	"""
	class Meta:
		unique_together = ('trail',)
	"""

	def __str__(self):
		return '%s %s' % (self.description, self.image)
