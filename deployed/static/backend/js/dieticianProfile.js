
function update(did){
    var jqXHR = $.ajax({
        type: "POST",
        url: "https://butternaan.herokuapp.com/dieticianProfile",
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