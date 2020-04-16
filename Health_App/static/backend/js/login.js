var userData = new Array()
function getUserData(username, password){
    var jqXHR = $.ajax({
        type: "POST",
        url: "http://0.0.0.0:5000/login",
        async: false,
        data: { user: username,
                pass: password },
        success: function(data) {
            if(data.listData.length!=0)
                window.location.href = "dash";
            else
                window.location.href = "login"
        }
    });
    // console.log(userData)
    // return jqXHR.responseText;
    // return userData;
}

document.getElementById("login_btn").onclick = function() {login()};


function login() {
	username = document.getElementById("username").value;
	password = document.getElementById("password").value;
	userData = getUserData(username, password);
}