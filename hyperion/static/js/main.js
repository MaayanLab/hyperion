function main(results) {

    Highcharts.setOptions({
        colors: ['#50B432', '#ED561B', '#DDDF00', '#24CBE5', '#64E572', '#FF9655', '#FFF263', '#6AF9C4']
    });

    var categories = [],
        series = [
            {
                name: 'passing',
                data: []
            },
            {
                name: 'failing',
                data: []
            }
        ];

    $.each(results, function(appIdx, result) {
        categories.push(result.app);
        $.each(result.tests, function(j, test) {
            if (test.status === 'passing') {
                add(series[0].data, appIdx);
            } else {
                add(series[1].data, appIdx);
            }
        });
    });

    function add(arr, i) {
        if (typeof arr[i] !== 'undefined') {
            arr[i] += 1;
        } else {
            arr[i] = 1;
        }
    }

    $('#bar-chart').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: ''
        },
        xAxis: {
            categories: categories
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Tests'
            },
            stackLabels: {
                enabled: true,
                style: {
                    fontWeight: 'bold',
                    color: (Highcharts.theme && Highcharts.theme.textColor) || 'gray'
                }
            }
        },
        legend: {
            align: 'right',
            x: -30,
            verticalAlign: 'top',
            y: 25,
            floating: true,
            backgroundColor: (Highcharts.theme && Highcharts.theme.background2) || 'white',
            borderColor: '#CCC',
            borderWidth: 1,
            shadow: false
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.x + '</b><br/>' +
                    this.series.name + ': ' + this.y + '<br/>' +
                    'Total: ' + this.point.stackTotal;
            }
        },
        plotOptions: {
            column: {
                stacking: 'normal'
            }
        },
        series: series
    });
}