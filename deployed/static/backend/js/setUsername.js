userData = new Array()
userDailyData = new Array()
var name = $.ajax({
        type: "POST",
        url: "https://butternaan.herokuapp.com/index",
        async: false,
        success: function(data) {
            userData = data.listData
        }
    });
// console.log(userData);

var nameSpan = document.getElementById("loggedUser");
temp = "";
nameSpan.innerText = temp.concat(userData[1], " ", userData[2]);