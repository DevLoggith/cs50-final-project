// TODO: Make charts responsive
// TODO: limit data down to 5-10 elemts with a value of 1?

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawCharts);

function drawCharts() {
    drawColumnChart();
    drawPieChart();
}

function drawColumnChart() {
    const data = google.visualization.arrayToDataTable(chartData)
    data.sort([{column: 1, desc: true}]);

    const barOptions = {
        title: '',
        chartArea: {width: '100%'},
        hAxis: {
            // title: 'Technology',
            minValue: 0
        },
        vAxis: {
            title: 'Count'
        }
    };

    const columnChart = new google.visualization.ColumnChart(document.getElementById('bar_chart'));
    columnChart.draw(data, barOptions);
}

function drawPieChart() {
    const data = google.visualization.arrayToDataTable(chartData)
    data.sort([{column: 1, desc: true}]);

    const pieOptions = {
        title: '',
        pieHole: 0.4
    };

    const pieChart = new google.visualization.PieChart(document.getElementById('pie_chart'));
    pieChart.draw(data, pieOptions);
} 

window.addEventListener('resize', function() {
    // Redraw your chart here
    drawCharts();
  });
