document
	.getElementById("location-button")
	.addEventListener("click", getLocation);

function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition((position) => {
			const latitude = position.coords.latitude;
			const longitude = position.coords.longitude;
			console.log(`${latitude}, ${longitude}`);
			sendLocationToServer(latitude, longitude);
		}, handleError);
	} else {
		console.log("Geolocation is not supported by this browser.");
	}
}

// URL endpoint needed for OSM Nominatim:
// https://nominatim.openstreetmap.org/reverse?format=json&lat=<value>&lon=<value>&zoom=10
// be sure to specify 'format=json' and 'zoom=10'. granularity only down to city level
// need to extract 'name' amd 'state'. [address][city] key is not always 'city' sometimes = town or municipality

// TODO: rewrite sendLocationToServer as reverseGeocode. use OSM Nom API to translate lat, lon > City, ST
// also have it contain logic to place reverseGeocode return value in location field, or abstract to helper function?
async function sendLocationToServer(latitude, longitude) {
	try {
		const response = await fetch("/scrape", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({ latitude: latitude, longitude: longitude }),
		});
		const data = await response.json();
		console.log("location saved:", data);
	} catch (error) {
		console.log("Error: ", error);
	}
}

function handleError(error) {
	switch (error.code) {
		case error.PERMISSION_DENIED:
			console.log("User denied the request for Geolocation.");
			break;
		case error.POSITION_UNAVAILABLE:
			console.log("Location information is unavailable.");
			break;
		case error.TIMEOUT:
			console.log("The request to get user location timed out.");
			break;
		case error.UNKNOWN_ERROR:
			console.log("An unknown error occurred.");
			break;
	}
}
