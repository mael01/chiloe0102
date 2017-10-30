# ChiloeSmart
	Plataforma desarrollada con el fin de poder mostrar los lugares más hermosos de Chiloé incluyendo un mapa con todos los lugares que un turista deberia conocer, actualmente se esta trabajando solo con lugares de Ancud.
	En este repositorio se podra encontrar una api desarrollada con django REST framework, la cual es utilizada sin autenticación dentro del proyecto, pero pronto se implementara Oauth2.
	La plataforma debe estar disponible por lo menos en 2 idiomas por lo que actualmente se trabaja con español e ingles.

# Backend
	Python3
	Django
	Django REST framework
	
# Frontend
	Javascript
	CSS3
	Materialize Framework
	Leaflet con Mapbox

# Idiomas
	Español
	Ingles

# Uso API
	En las consultas de la api, estas devolveran las coordenadas para trabajar con mapas, en este proyecto se utilizo leaflet con mapbox.
	Consultas:
	/rest_chiloe/hola/  entra un saludos "Hola mundo"
	/rest_chiloe/ciudades/ entrega toda la información de todas las ciudades registradas
	/rest_chiloe/ciudades/id/ entrega toda la información de una ciudad - id



