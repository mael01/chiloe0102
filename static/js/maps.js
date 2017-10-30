$(document).ready(function(){
	$("#eje").click(hideleftbar);

	var pathname = window.location.pathname;

	$("#btn_menu_map").click(muestraMenu);
	$(".button-collapse").sideNav();

	if(pathname == '/places/map/'){

		$.ajax({
			method: "GET",
			url: "/rest_chiloe/ciudades/1/?format=json"
		})
			.done(function (respuesta){
				var path_icons_round = "/static/img/maps/icons_rounds/";
				var mymap = L.map('maps').setView([-41.8720988, -73.8401218], 14);

				//if (mymap != undefined) { mymap.remove(); }

				L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v10/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFlbDkxIiwiYSI6ImNpd3Y0aWNvaDAwdTMyb3Fid254OThpOHoifQ.Xjhsjuvdqz3pwPxkK-wAbA', {
					attribution: 'Gracias Totales',
					maxZoom: 16,
				}).addTo(mymap);

				mymap.zoomControl.setPosition('topright');

				var markerIconPlace = L.Icon.extend({
					options: {
						iconSize:     [50, 90],
						iconAnchor:   [25, 90], // point of the icon which will correspond to marker's location
						popupAnchor:  [-3, -76]// point from which the popup should open relative to the iconAnchor
					}
				});

				var markerIconWidth = L.Icon.extend({
					options: {
						iconSize:     [140, 70],
						iconAnchor:   [120, 70], // point of the icon which will correspond to marker's location
						popupAnchor:  [-3, -76]// point from which the popup should open relative to the iconAnchor
					}
				});


				var iconBeach = new markerIconPlace({iconUrl: '/static/img/maps/icon_beach_1.png'});
				var iconLandscape = new markerIconPlace({iconUrl: '/static/img/maps/icon_landscape_1.png'});
				var iconTrail = new markerIconPlace({iconUrl: '/static/img/maps/icon_trail_1.png'});
				var iconHotel = new markerIconPlace({iconUrl: '/static/img/maps/btn_localizacion_hoteles.png'});
				var iconPolice = new markerIconWidth({iconUrl: '/static/img/maps/btn_localizacion_carabineros.png'});
				var iconHospital = new markerIconWidth({iconUrl: '/static/img/maps/btn_localizacion_hospital.png'});
				var iconCottage = new markerIconPlace({iconUrl: '/static/img/maps/btn_localizacion_cabanas.png'});
				var iconRentCar = new markerIconPlace({iconUrl: '/static/img/maps/btn_localizacion_rentacar.png'});
				var iconRestaurant = new markerIconPlace({iconUrl: '/static/img/maps/btn_localizacion_restaurant.png'});


				var playas = respuesta.beachs;
				var cabanas = respuesta.cottages;
				var landscapes = respuesta.landscapes;
				var trails = respuesta.trails;
				var hospitals = respuesta.hospitals;
				var hotels = respuesta.hotels;
				var polices = respuesta.polices;
				var rentcars = respuesta.rentcars;
				var restaurants = respuesta.restaurants;


				var arrMarkersBeach = [];
				var arrMarkersHotels = [];
				var arrMarkersRentacar = [];
				var arrMarkersCabanas = [];
				var arrMarkersLandscapes = [];
				var arrMarkersTrails = [];
				var arrMarkersRestaurant = [];

				for (var k = 0; k < playas.length; k++){
					L.icon = function (options) {
						return new L.Icon(options);
					};
					playas[k].iconRound = path_icons_round+"icon_beach_round.png";
					var thismarker = L.marker([playas[k].latitude, playas[k].longitue], {icon: iconBeach}).addTo(mymap).on('click', L.bind(clickMarker, null, playas[k]));
					arrMarkersBeach.push(thismarker);
				}

				for (var k = 0; k < cabanas.length; k++){
					L.icon = function (options) {
						return new L.Icon(options);
					};
					cabanas[k].iconRound = path_icons_round+"icon_cabanas_round.png";
					var thismarker = L.marker([cabanas[k].latitude, cabanas[k].longitue], {icon: iconCottage}).addTo(mymap).on('click', L.bind(clickMarker, null, cabanas[k]));
					arrMarkersCabanas.push(thismarker);
				}


				for (var k = 0; k < polices.length; k++){
					L.icon = function (options) {
						return new L.Icon(options);
					};
					polices[k].iconRound = path_icons_round+"icon_pcarab.png";
					L.marker([polices[k].latitude, polices[k].longitue], {icon: iconPolice}).addTo(mymap).on('click', L.bind(clickMarker, null, polices[k]));
				}

				for (var k = 0; k < landscapes.length; k++){
					L.icon = function (options) {
						return new L.Icon(options);
					};
					landscapes[k].iconRound = path_icons_round+"icon_landscape_round.png";
					var thismarker = L.marker([landscapes[k].latitude, landscapes[k].longitue], {icon: iconLandscape}).addTo(mymap).on('click', L.bind(clickMarker, null, landscapes[k]));
					arrMarkersLandscapes.push(thismarker);
				}

				for (var k = 0; k < trails.length; k++){
					L.icon = function (options) {
						return new L.Icon(options);
					};
					trails[k].iconRound = path_icons_round+"icon_trail_round.png";
					var thismarker = L.marker([trails[k].latitude, trails[k].longitue], {icon: iconTrail}).addTo(mymap).on('click', L.bind(clickMarker, null, trails[k]));
					arrMarkersTrails.push(thismarker);
				}

				for (var k = 0; k < hospitals.length; k++){
					L.icon = function (options) {
						return new L.Icon(options);
					};
					hospitals[k].iconRound = path_icons_round+"icon_hospita.png";
					L.marker([hospitals[k].latitude, hospitals[k].longitue], {icon: iconHospital}).addTo(mymap).on('click', L.bind(clickMarker, null, hospitals[k]));
				}

				for (var k = 0; k < hotels.length; k++){
					L.icon = function (options) {
						return new L.Icon(options);
					};
					hotels[k].iconRound = path_icons_round+"icon_hoteles_round.png";
					var thismarker = L.marker([hotels[k].latitude, hotels[k].longitue], {icon: iconHotel}).addTo(mymap).on('click', L.bind(clickMarker, null, hotels[k]));
					arrMarkersHotels.push(thismarker);
				}

				for (var k = 0; k < rentcars.length; k++){
					L.icon = function (options) {
						return new L.Icon(options);
					};
					rentcars[k].iconRound = path_icons_round+"icon_rentacar_round.png";
					var thismarker = L.marker([rentcars[k].latitude, rentcars[k].longitue], {icon: iconRentCar}).addTo(mymap).on('click', L.bind(clickMarker, null, rentcars[k]));
					arrMarkersRentacar.push(thismarker);
				}

				for (var k = 0; k < restaurants.length; k++){
					L.icon = function (options) {
						return new L.Icon(options);
					};
					restaurants[k].iconRound = path_icons_round+"icon_restaurantes_round.png";
					var thismarker = L.marker([restaurants[k].latitude, restaurants[k].longitue], {icon: iconRestaurant}).addTo(mymap).on('click', L.bind(clickMarker, null, restaurants[k]));
					arrMarkersRestaurant.push(thismarker);
				}

				$("#btn_addelete_beach").click({'mymap': mymap, 'arrMarkers': arrMarkersBeach}, AddOrDeleteMarker);
				$("#btn_addelete_hotels").click({'mymap': mymap, 'arrMarkers': arrMarkersHotels}, AddOrDeleteMarker);
				$("#btn_addelete_rentacar").click({'mymap': mymap, 'arrMarkers': arrMarkersRentacar}, AddOrDeleteMarker);
				$("#btn_addelete_cabanas").click({'mymap': mymap, 'arrMarkers': arrMarkersCabanas}, AddOrDeleteMarker);
				$("#btn_addelete_landscapes").click({'mymap': mymap, 'arrMarkers': arrMarkersLandscapes}, AddOrDeleteMarker);
				$("#btn_addelete_trails").click({'mymap': mymap, 'arrMarkers': arrMarkersTrails}, AddOrDeleteMarker);
				$("#btn_addelete_restaurant").click({'mymap': mymap, 'arrMarkers': arrMarkersRestaurant}, AddOrDeleteMarker);
				//getAllMarkers(mymap);

		});
		
	}

});

var clickMarker = function (e) {

	$("#hola")
		.html('<div id="modal1" class="modal">\
					<div class="col s12 m12">\
						<div class="card medium" style="margin: 0 !important;">\
							<div class="card-image">\
								<img src="/'+e.img_refer+'">\
								<span class="card-title"><h5>'+e.name+'</h5></span>\
							</div>\
							<img class="img-card-custom" src="'+e.iconRound+'">\
							<div class="card-content">\
								<p>'+e.description+'</p>\
							</div>\
						</div>\
					</div>\
				</div>');

	$('#modal1').openModal()

	if(e.img_place.length == 0){
		$('#img_carousel').append('No hay imagenes disponibles');
	}else{
		for(var i = 0; i < e.img_place.length; i++){
			$('#img_carousel').append('<a class="carousel-item" style="height: 0 !important;"><img src="/'+e.img_place[i].image+'""></a>');
		}
	}
	
	$('.carousel').carousel();

	$('.carousel-item').click(function(){
		var img_place = $(this).find('img');
		var img_place_elem = img_place[0].src;

		$('#div-img').html('<div id="modal2" class="modal">\
					<div class="modal-content">\
						<div class="row no-margin-bottom">\
							<div id="add_img_place" class="add_img_place col m4">\
								<img src="'+img_place_elem+'">\
							</div>\
						</div>\
					</div>\
				</div>');

		$('#modal2').openModal();
	});

}


var muestraMenu = function(e){
	var myMenu = $("#menu-map-places");
	myMenu.addClass('animated fadeInRight');
	myMenu.show();

	$("body").css("overflow", "hidden");
	$(".container-menu-map-places").addClass("add-zindex");
	divcontainermenu = $(".container-menu-map-places");

	if(window.onclick = function(event) {
		if (event.target.id == divcontainermenu[0].id) {
			myMenu.hide();
			divcontainermenu.removeClass("add-zindex");
		}
	});

}

var AddOrDeleteMarker = function (e){
	var map = e.data.mymap;
	var markers = e.data.arrMarkers;

	if($(this).attr('estadoMarkers') == "borrados"){
		for(var i = 0; i < markers.length; i++){
			markers[i].addTo(map);
		}
		$(this).attr('estadoMarkers', 'agregados');
	}else{
		for(var i = 0; i < markers.length; i++){
			map.removeLayer(markers[i]);
		}
		$(this).attr('estadoMarkers', 'borrados');
	}
}

var hideleftbar = function(){

	if($("#side-bar-left").hasClass('escondido')){

		$("#side-bar-left").removeClass('escondido');
		$("#side-bar-left").animate({
			"left": "+=280px"
		}, "slow");

		$(this).animate({
			"left": "+=225px"
		}, "slow");
		

	}else{

		$("#side-bar-left").addClass('escondido');
		$("#side-bar-left").animate({
			"left": "-=280px"
		}, "slow");

		$(this).animate({
			"left": "-=225px"
		}, "slow");


	}
}