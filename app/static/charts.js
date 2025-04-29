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
            case 30: color = 'color: #1A1A7E'; break;
            case 29: color = 'color: #0047AB'; break;
            case 28: color = 'color: #0096FF'; break;
            case 27: color = 'color: #008080'; break;
            case 26: color = 'color: #00C2A8'; break;
            case 25: color = 'color: #32CD32'; break;
            case 24: color = 'color: #228B22'; break;
            case 23: color = 'color: #66AA00'; break;
            case 22: color = 'color: #DAA520'; break;
            case 21: color = 'color: #FFD700'; break;
            case 20: color = 'color: #FF7300'; break;
            case 19: color = 'color: #CC5500'; break;
            case 18: color = 'color: #FFB300'; break;
            case 17: color = 'color: #8B4000'; break;
            case 16: color = 'color: #FF2400'; break;
            case 15: color = 'color: #FF4500'; break;
            case 14: color = 'color: #8B0707'; break;
            case 13: color = 'color: #B22222'; break;
            case 12: color = 'color: #C2185B'; break;
            case 11: color = 'color: #DD4477'; break;
            case 10: color = 'color: #9400D3'; break;
            case 9: color = 'color: #6A0DAD'; break;
            case 8: color = 'color: #FF00FF'; break;
            case 7: color = 'color: #4B0082'; break;
            case 6: color = 'color: #0F52BA'; break;
            case 5: color = 'color: #007BA7'; break;
            case 4: color = 'color: #1C39BB'; break;
            case 3: color = 'color: #00CED1'; break;
            case 2: color = 'color: #109618'; break;
            default: color = 'color: grey';
        }
        data.addRow([row[0], row[1], color]);
    };

    data.sort([{column: 1, desc: true}]);

    const columnOptions = {
        title: 'Tech Skills Column Chart',
        legend: { position: 'none' },
        bars: 'vertical',
        bar: { groupWidth: '70%' },
        colors: ['#4285f4'],
        chartArea: { width: '96%', height: '70%' },
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
        title: 'Tech Skills Donut Chart',
        pieHole: 0.4,
        sliceVisibilityThreshold: 1/64,
        chartArea: { top: '50', width: '100%'},
        legend: { position: 'bottom'}
    };

    const pieChart = new google.visualization.PieChart(document.getElementById('pie_chart'));
    pieChart.draw(data, pieOptions);
} 

window.addEventListener('resize', function() {
    drawCharts();
  });
