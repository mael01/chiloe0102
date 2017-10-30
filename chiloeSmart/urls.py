"""chiloeSmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, handler400, handler403, handler404, handler500
from django.contrib import admin
from places import views as places_views
from django.views.i18n import javascript_catalog


    

handler400 = places_views.bad_request
#handler403 = places_views.permission_denied
handler404 = places_views.page_not_found
handler500 = places_views.server_error

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('',),
}

urlpatterns = [
    url(r'^$', places_views.start, name='index_places'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict, name='javascript-catalog'),
    url(r'^admin/', admin.site.urls),
    #url(r'^start/', places_views.start, name = 'start'),
    #url(r'^home/', places_views.home, name = 'index_places'),
    url(r'^places/beachs/$', places_views.home_beach, name = 'home_places_beachs'),
    url(r'^places/trails/$', places_views.home_trails, name = 'home_places_trails'),
    url(r'^places/landsc/$', places_views.home_landscapes, name = 'home_places_landscapes'),
    url(r'^places/map/$', places_views.home_map_city, name = 'home_map_city'),
    #url(r'^places/getallplaces/', places_views.get_locations, name = 'get_locations'),

    url(r'^rest_chiloe/', include('apichiloe.urls')),
]
