$(document).ready(function(){
		$('select').material_select();
		$('.materialboxed').materialbox();
		$('.scrollspy').scrollSpy({scrollOffset: 0,});
		$('.carousel.carousel-slider').carousel({full_width: true, duration:300, indicators:true,shift:0,padding:0,});
		$("#start_session").on("click", clickHome);
		$("#arrow_start_session").on("click", clickHome);

		
		$(window).scroll(function(){
		if ($(this).scrollTop() > 100) {
				$('#btn_up').fadeIn();
			} else {
				$('#btn_up').fadeOut();
			}
		});
		
		//Click event to scroll to top
		$('#btn_up').click(function(){
			$('html, body').animate({scrollTop : 0},800);
			return false;
		});

		$(".get_modal").on('click', function(e){
			$('#test_modal').openModal();
			var holi = $(this).data("place");
			console.log(holi);
		});

		
		$(".btn-circle-close").on('click', function(e){
			$('#test_modal').closeModal();
		})

		var myses = sessionStorage.getItem("visita");
		var pathname = window.location.pathname;

		if(myses != null){
			var jsonSesion = $.parseJSON(myses);
			if (pathname != '/start/'){
				if (pathname != '/home/'){
					sessionStorage.removeItem('visita');
					jsonSesion[pathname] = pathname;
					sessionStorage.setItem("visita", JSON.stringify(jsonSesion));
				}
			}
			console.log(jsonSesion);
		}else{
			console.log("No hay sesion");
		}

		var $grid = $('.grid').masonry({
			itemSelector: '.grid-item',
			percentPosition: true,
			columnWidth: '.grid-sizer',
		});
		// layout Masonry after each image loads
		$grid.imagesLoaded().progress( function() {
			$grid.masonry();
		});



});


var mysession = function(home){
	this.inicio = home;
};


var clickHome = function(){
    if(typeof(Storage) !== "undefined") {
    	var session = new mysession("Home");
    	var ses = sessionStorage.setItem("visita", JSON.stringify(session));
    } else {
        document.getElementById("result").innerHTML = "Sorry, your browser does not support web storage...";
    }
};