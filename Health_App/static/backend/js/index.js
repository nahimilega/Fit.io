userData = new Array()
userDailyData = new Array()
var name = $.ajax({
        type: "POST",
        url: "http://0.0.0.0:5000/index",
        async: false,
        success: function(data) {
            userData = data.listData
        }
    });
// console.log(userData);

var nameSpan = document.getElementById("loggedUser");
temp = "";
nameSpan.innerText = temp.concat(userData[1], " ", userData[2]);

var dailyrecord = $.ajax({
        type: "POST",
        url: "http://0.0.0.0:5000/index/getmoreinfo",
        async: false,
        success: function(data) {
            userDailyData = data.daily
        }
    });
console.log(userDailyData);

var length = userDailyData.length - 1;

var heartRate = userDailyData[length][3];
var calorie = userDailyData[length][2];
var weight = userDailyData[length][4];
var stepCount = userDailyData[length][1];

console.log(heartRate);
console.log(calorie);
console.log(weight);
console.log(stepCount);

var heartHeading = document.getElementById("heartRate");
heartHeading.innerText = heartRate;

var stepHeading = document.getElementById("stepCount");
stepHeading.innerText = stepCount;

var calorieHeading = document.getElementById("calorie");
calorieHeading.innerText = calorie;

var weightHeading = document.getElementById("weight");
weightHeading.innerText = weight;