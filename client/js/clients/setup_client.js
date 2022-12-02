console.log("LOAD SETUP CLIENT")


function postCheckSetup(ip){
    if(request.readyState == 4) {
        console.log(ip)
        if(request.status == 409) {
            alert("Your setup is already complete, redirecting to home page")
            redirectToHome(ip)
        } else {
            console.log("Setup is not yet done.")
        }
    }
}


function checkSetup(ip){
  if(window.XMLHttpRequest){
    request=new XMLHttpRequest();
   }
   else if(window.ActiveXObject){
    request=new ActiveXObject("Microsoft.XMLHTTP");
   }

   try  {
     console.log('preparing request')
     request.open("GET",`http://${ip}:5000/is_fresh_install`,true);
     request.onreadystatechange=function(){postCheckSetup(ip)}
     request.setRequestHeader("Content-Type", "application/json");
     request.send();
   }
   catch(e) {
    alert('something went wrong');
   }
}

function postSendSetup(ip){
    if(request.readyState == 4) {
        console.log(ip)
        if(request.status != 200) {
            alert("Password did not match password requirements.")
        } else {
            alert("Setup Complete! Redirecting to home.")
             redirectToHome(ip)
        }
    }
}


function sendSetupRequest(ip){
  if(window.XMLHttpRequest){
    request=new XMLHttpRequest();
   }
   else if(window.ActiveXObject){
    request=new ActiveXObject("Microsoft.XMLHTTP");
   }
     console.log('preparing request')
     request.open("POST",`http://${ip}:5000/setup`,true);
     request.setRequestHeader("Content-Type", "application/json");
     request.send(JSON.stringify({pw: document.getElementById('masterkey').value}));
     request.onreadystatechange=function(){postSendSetup(ip)}
     request.setRequestHeader("Content-Type", "application/json");
     request.send();

}
