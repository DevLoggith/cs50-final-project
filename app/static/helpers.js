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

async function sendLocationToServer(latitude, longitude) {
	try {
		const response = await fetch("/save_location", {
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

export { handleError, sendLocationToServer };
