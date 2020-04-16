$(document).ready(function() {

    // Bar Chart - 1

    var barChartData = {
        labels: ['March 24', 'March 25', 'March 26', 'March 27', 'March 28', 'March 29'],
        datasets: [{
            label: 'Calories Consumed',
            backgroundColor: 'rgba(0, 158, 251, 0.5)',
            borderColor: 'rgba(0, 158, 251, 1)',
            borderWidth: 1,
            data: [4010, 2910, 3509, 2656, 4528, 3103, 40]
        }, {
            label: 'Calories Burnt',
            backgroundColor: 'rgba(255, 188, 53, 0.5)',
            borderColor: 'rgba(255, 188, 53, 1)',
            borderWidth: 1,
            data: [2350, 1945, 2900, 1910, 4028, 1802, 90]
        }]
    };

    var ctx = document.getElementById('bargraph').getContext('2d');
    window.myBar = new Chart(ctx, {
        type: 'bar',
        data: barChartData,
        options: {
            responsive: true,
            legend: {
                display: false,
            }
        }
    });

    // Bar Chart - 2

    var barChartData1 = {
        labels: ['March 22', 'March 23', 'March 24', 'March 25', 'March 26', 'March 27', 'March 28', 'March 29'],
        datasets: [{
            label: 'No. of Steps',
            backgroundColor: 'rgba(0, 158, 251, 0.5)',
            borderColor: 'rgba(0, 158, 251, 1)',
            borderWidth: 1,
            data: [3010, 4052, 5509, 2956, 4528, 3603, 4925, 4348]
        }]
    };

    var ctx1 = document.getElementById('bargraph1').getContext('2d');
    window.myBar = new Chart(ctx1, {
        type: 'bar',
        data: barChartData1,
        options: {
            responsive: true,
            legend: {
                display: false,
            }
        }
    });

    // Bar Chart 2

    barChart();

    $(window).resize(function() {
        barChart();
    });

    function barChart() {
        $('.bar-chart').find('.item-progress').each(function() {
            var itemProgress = $(this),
                itemProgressWidth = $(this).parent().width() * ($(this).data('percent') / 100);
            itemProgress.css('width', itemProgressWidth);
        });
    };
});