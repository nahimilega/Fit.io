var allDietitian = $.ajax({
        type: "POST",
        url: "http://0.0.0.0:5000/dieticians",
        async: false,
        success: function(data) {
            userDailyData = data.daily
        }
});