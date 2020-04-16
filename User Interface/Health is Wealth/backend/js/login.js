var userData = new Array()
function getUserData(username, password){
    var jqXHR = $.ajax({
        type: "POST",
        url: "http://0.0.0.0:5000/login",
        async: false,
        data: { user: username,
                pass: password },
        success: function(data) {
            userData = data.listData
        }
    });
    console.log(userData)
    // return jqXHR.responseText;
    return userData;
}

document.getElementById("login_btn").onclick = function() {login()};


function login() {
	username = document.getElementById("username").value
	password = document.getElementById("password").value
	result = getUserData(username, password)
    JSON.stringify(result)
    if(result.length!=0)
        window.location.assign("index.html");
    else
        window.location.assign("login.html");



}