import * as helpers from "./helpers.js";

function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition((position) => {
			const latitude = position.coords.latitude;
			const longitude = position.coords.longitude;
			console.log(`Longitude: ${longitude} Latitude: ${latitude}`);
			helpers.sendLocationToServer(latitude, longitude);
		}, helpers.handleError);
	} else {
		console.log("Geolocation is not supported by this browser.");
	}
}

document
	.getElementById("location-button")
	.addEventListener("click", getLocation);
