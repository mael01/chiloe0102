var idleTime = 0;

	//Increment the idle time counter every minute.
	idleInterval = setInterval(timerIncrement, 20000); // 2 minutes

	//Zero the idle timer on mouse movement.
	$('body').mousemove(function (e) {
	//alert("mouse moved" + idleTime);
	idleTime = 0;
	});

	$('body').keypress(function (e) {
	//alert("keypressed"  + idleTime);
	idleTime = 0;
	});

	$('body').click(function () {
		//alert("mouse moved" + idleTime);
		idleTime = 0;
	});

function timerIncrement () {
	idleTime = idleTime + 1;
	if (idleTime > 1000) { // 10 minutes
		var i = sessionStorage.length;
		while(i--) {
			var key_session = sessionStorage.key(i);

			if(key_session != null){
				console.log("Sesion en el timer: "+key_session);
				sessionStorage.removeItem(key_session);

				//Aca guardo la sesion en la bd

			}else{
				console.log("No hay sesion en el timer");
			}

		}
		window.location.assign("/start/");
	}
}