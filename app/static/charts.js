// TODO: Make charts responsive
// TODO: limit data down to 5-10 elements with a value of 1?

google.charts.load('current', {'packages':['bar']});
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawCharts);

function drawCharts() {
    drawColumnChart();
    drawPieChart();
}

function drawColumnChart() {
    const data = new google.visualization.DataTable()
    data.addColumn('string', 'Technology');
    data.addColumn('number', 'Count');
    data.addColumn({type: 'string', role: 'style'});

    for (let i = 0; i < chartData.length; i++) {
        const row = chartData[i];
        let color;
        switch(row[1]) {
            case 10: color = 'color: #A29BFE'; break;
            case 9: color = 'color: #FD79A8'; break;
            case 8: color = 'color: #E74C3C'; break;
            case 7: color = 'color: #E67E22'; break;
            case 6: color = 'color: #F1C40F'; break;
            case 5: color = 'color: #2ECC71'; break;
            case 4: color = 'color: #1ABC9C'; break;
            case 3: color = 'color: #3498DB'; break;
            case 2: color = 'color: #2C3E50'; break;
            default: color = 'color: grey';
        }
        data.addRow([row[0], row[1], color]);
    };

    data.sort([{column: 1, desc: true}]);

    const columnOptions = {
        title: 'Technology Count',
        legend: { position: 'none' },
        bars: 'vertical',
        bar: { groupWidth: '85%' },
        colors: ['#4285f4'], // Default color (will be overridden by your style role)
        // Modern styling options
        chartArea: { width: '80%', height: '70%' },
        backgroundColor: { fill: 'transparent' },
        animation: {
          startup: true,
          duration: 500,
          easing: 'out'
        }
      };

    const columnChart = new google.visualization.ColumnChart(document.getElementById('column_chart'));
    columnChart.draw(data, columnOptions);
}

function drawPieChart() {
    const data = new google.visualization.DataTable()
    data.addColumn('string', 'Technology');
    data.addColumn('number', 'Count');
    chartData.forEach(function(row) {
        data.addRow([row[0], row[1]])
    });

    data.sort([{column: 1, desc: true}]);

    const pieOptions = {
        title: '',
        pieHole: 0.4,
        sliceVisibilityThreshold: 1/64
    };

    const pieChart = new google.visualization.PieChart(document.getElementById('pie_chart'));
    pieChart.draw(data, pieOptions);
} 

window.addEventListener('resize', function() {
    drawCharts();
  });
