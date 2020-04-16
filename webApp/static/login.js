function runPyScript(input){
            var jqXHR = $.ajax({
                type: "POST",
                url: "http://0.0.0.0:5000/login",
                async: false,
                data: { mydata: input }
            });

            return jqXHR.responseText;
        }

$('#loginButton').click(function(){
    datatosend = document.getElementById("username").value;
    username=document.getElementById("username").value;
    password=document.getElementById("password").value
    
    if(username!="" && password!=""){
        result = runPyScript(datatosend);
        console.log('Got back ' + result);
    }
   document.getElementById("username").value=null;
   document.getElementById("password").value=null; 
});

console.log("world");