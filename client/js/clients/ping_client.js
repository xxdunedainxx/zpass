console.log("LOAD PING CLIENT")

function postPing(){
    if(request.readyState == 4) {
        if(request.status != 200) {
            alert("Something is wrong with the backend server, ping check failed")
        } else {
            console.log("Ping check passed")
        }
    }
}


function pingCheckServer(ip){
  if(window.XMLHttpRequest){
    request=new XMLHttpRequest();
   }
   else if(window.ActiveXObject){
    request=new ActiveXObject("Microsoft.XMLHTTP");
   }

   try  {
     console.log('preparing request')
     request.open("GET",`http://${ip}:5000/ping`,true);
     request.onreadystatechange=postPing(ip)
     request.setRequestHeader("Content-Type", "application/json");
     request.send();
   }
   catch(e) {
    alert('something went wrong');
   }
}