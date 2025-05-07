google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(drawCharts);

function drawCharts() {
	const screenWidth = window.innerWidth;
	drawColumnChart(screenWidth);
	drawPieChart(screenWidth);
}

// Helper function to get color based on count value
function getColorForCount(count) {
	switch (count) {
		case 30: return "color: #1A1A7E";
		case 29: return "color: #0047AB";
		case 28: return "color: #0096FF";
		case 27: return "color: #008080";
		case 26: return "color: #00C2A8";
		case 25: return "color: #32CD32";
		case 24: return "color: #228B22";
		case 23: return "color: #66AA00";
		case 22: return "color: #DAA520";
		case 21: return "color: #FFD700";
		case 20: return "color: #FF7300";
		case 19: return "color: #CC5500";
		case 18: return "color: #FFB300";
		case 17: return "color: #8B4000";
		case 16: return "color: #FF2400";
		case 15: return "color: #FF4500";
		case 14: return "color: #8B0707";
		case 13: return "color: #B22222";
		case 12: return "color: #C2185B";
		case 11: return "color: #DD4477";
		case 10: return "color: #9400D3";
		case 9: return "color: #6A0DAD";
		case 8: return "color: #FF00FF";
		case 7: return "color: #4B0082";
		case 6: return "color: #0F52BA";
		case 5: return "color: #007BA7";
		case 4: return "color: #1C39BB";
		case 3: return "color: #00CED1";
		case 2: return "color: #109618";
		default: return "color: grey";
	}
}

// Helper function to create a DataTable from chart data
function createDataTableFromChartData(sourceData, limit = null) {
    const dataTable = new google.visualization.DataTable();
    dataTable.addColumn("string", "Technology");
    dataTable.addColumn("number", "Count");
    dataTable.addColumn({ type: "string", role: "style" });

    let processedData = sourceData.slice(); // makes shallow copy of sourceData
    processedData.sort((a, b) => b[1] - a[1]); // sort by count, descending
    
    if (limit) {
        processedData = processedData.slice(0, limit); // take only top n items
    }

	processedData.forEach(row => {
		dataTable.addRow([row[0], row[1], getColorForCount(row[1])]);
	});

    return dataTable;
}

function drawColumnChart(screenWidth) {
	// Base options for column chart (& for every device over 1024px wide)
	const columnOptions = {
		title: "Tech Skills Column Chart",
		hAxis: { 
			title: "Technology Names",
			slantedText: true,
			slantedTextAngle: 45 
		},
		vAxis: {
			title: "Times Mentioned in Job Descriptions",
			format: "#",
		},
		legend: { position: "none" },
		bar: { groupWidth: "70%" },
		chartArea: { width: "92%", height: "70%" },
		animation: {
			startup: true,
			duration: 500,
			easing: "out",
		},
	};

	if (screenWidth < 768) {
		columnOptions.chartArea = { width: "80%", height: "60%" };
		columnOptions.bar.groupWidth = "85%";
		columnOptions.hAxis.slantedText = true;
		columnOptions.hAxis.slantedTextAngle = 90;
		columnOptions.hAxis.textStyle = { fontSize: 11 };
		
		// On mobile, create a datatable with only top 15 items
		const data = createDataTableFromChartData(chartData, 15);
		columnOptions.title += " (Top 15)";
		
		const columnChart = new google.visualization.ColumnChart(
			document.getElementById("column_chart")
		);
		columnChart.draw(data, columnOptions);

	} else {
		if (screenWidth < 1024) {
			columnOptions.chartArea = { width: "90%", height: "65%" };
			columnOptions.hAxis.slantedText = true;
			columnOptions.hAxis.slantedTextAngle = 55;
		}
		// Create full data table
		const data = createDataTableFromChartData(chartData);
		
		const columnChart = new google.visualization.ColumnChart(
			document.getElementById("column_chart")
		);
		columnChart.draw(data, columnOptions);
	}
}

function drawPieChart(screenWidth) {
	// Create the data table for the pie chart
	const dataTable = new google.visualization.DataTable();
	dataTable.addColumn("string", "Technology");
	dataTable.addColumn("number", "Count");
	
	chartData.forEach(row => {
		dataTable.addRow([row[0], row[1]]);
	});

	dataTable.sort([{ column: 1, desc: true }]);

	// Base options for pie chart
	const pieOptions = {
		title: "Tech Skills Donut Chart",
		pieHole: 0.4,
		sliceVisibilityThreshold: 1 / 64,
	};

	if (screenWidth < 992) {
		pieOptions.chartArea = { top: "50", width: "100%" };
		pieOptions.legend = { position: "bottom" };
	}

	const pieChart = new google.visualization.PieChart(
		document.getElementById("pie_chart")
	);
	pieChart.draw(dataTable, pieOptions);
}

window.addEventListener("resize", drawCharts);