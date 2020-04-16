var userDailyData = new Array();
var dailyrecord = $.ajax({
        type: "POST",
        url: "http://0.0.0.0:5000/index/getmoreinfo",
        async: false,
        success: function(data) {
            userDailyData = data.daily
        }
    });
console.log(userDailyData);

var l = userDailyData.length-1;
var date1 = userDailyData[l][0].slice(5, 11);
var date2 = userDailyData[l-1][0].slice(5, 11);
var date3 = userDailyData[l-2][0].slice(5, 11);
var date4 = userDailyData[l-3][0].slice(5, 11);
var date5 = userDailyData[l-4][0].slice(5, 11);




$(document).ready(function() {

    // Bar Chart - 1

    var barChartData = {
        labels: [date1, date2, date3, date4, date5],
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
        labels: [date1, date2, date3, date4, date5],
        datasets: [{
            label: 'No. of Steps',
            backgroundColor: 'rgba(0, 158, 251, 0.5)',
            borderColor: 'rgba(0, 158, 251, 1)',
            borderWidth: 1,
            data: [userDailyData[l][1], userDailyData[l-1][1], userDailyData[l-2][1], userDailyData[l-3][1], userDailyData[l-4][1]]
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