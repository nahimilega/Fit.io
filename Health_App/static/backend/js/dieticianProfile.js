
function update(did){
    var jqXHR = $.ajax({
        type: "POST",
        url: "http://0.0.0.0:5000/dieticianProfile",
        async: false,
        data: { "did": did},
        success: function(data) {
            console.log("complete")
        }
    });
}

document.getElementById("chooseDietician").onclick = function() {choose()};


function choose() {
    console.log("inside");
    dieiticianData = document.getElementById("dieticianID").innerHTML;
    dieiticianData = dieiticianData.split(" ");
    dieiticianID = dieiticianData[dieiticianData.length-1];
    userData = update(dieiticianID);
}