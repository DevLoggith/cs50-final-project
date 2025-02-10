document
	.getElementById("location-button")
	.addEventListener("click", getLocation);

function getLocation() {
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(async (position) => {
			const latitude = position.coords.latitude;
			const longitude = position.coords.longitude;
			const location = await reverseGeocode(latitude, longitude);
			if (location) {
				// TODO: create helper function to place location.city,
				// location.state in 'location' text field
				console.log("City:", location.city);
				console.log("State:", location.state);
			}
		}, handleError);
	} else {
		console.log("Geolocation is not supported by this browser.");
	}
}

async function reverseGeocode(latitude, longitude) {
	// see Nominatim docs for info regarding the usage of different parameters
	// https://nominatim.org/release-docs/develop/api/Reverse/
	const endpoint = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${latitude}&lon=${longitude}&zoom=10`;
	try {
		const response = await fetch(endpoint, {
			headers: {
				"User-Agent": NOMINATIM_USER_AGENT
			}
		});
		if (!response.ok) {
			throw new Error("HTTP error. Status: ${response.status}");
		}
		const data = await response.json();
		const address = data.address;
		const city = data.name;
		const state = address.state;

		return { city, state };
	} catch (error) {
		console.log("Error during reverse geocoding: ", error);
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
