function updateUserData(firstName, lastName, DOB, address, contact, weight){
    var jqXHR = $.ajax({
        type: "POST",
        url: "https://butternaan.herokuapp.com/editprofile",
        async: false,
        data: { "firstName": firstName,
                "lastName": lastName,
                "DOB": DOB,
                "address": address,
                "contact": contact,
                "weight": weight },
        success: function(data) {
            if(data.updated=="True")
                window.location.href = "editprofile";
        }
    });

}




document.getElementById("save_btn").onclick = function() {save()};

function save() {
    firstName = document.getElementById("firstName").value;
    lastName = document.getElementById("lastName").value;
    DOB = document.getElementById("DOB").value
    address = document.getElementById("address").value.concat(", ", document.getElementById("state").value, "-", document.getElementById("pincode").value, ", ", document.getElementById("country").value)
    contact = document.getElementById("contact").value
    weight = document.getElementById("weight").value
    console.log(firstName)
    console.log(lastName)
    console.log(DOB)
    console.log(address)
    console.log(contact)
    console.log(weight)

    userData = updateUserData(firstName, lastName, DOB, address, contact, weight);
}