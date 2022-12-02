console.log('HOME CLIENT LOADED')

function postCheckSetup(ip){
    if(request.readyState == 4) {
        console.log(ip)
        if(request.status != 409) {
            alert("Your setup is not complete, redirecting to setup page")
            redirectToSetup(ip)
        } else {
            console.log("Setup has been verified.")
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

function submitMasterkey(ip) {
  console.log('Submitting master key...')
  if(window.XMLHttpRequest){
    request=new XMLHttpRequest();
   }
   else if(window.ActiveXObject){
    request=new ActiveXObject("Microsoft.XMLHTTP");
   }

   try  {
     console.log('preparing request')
     request.onreadystatechange=getInfo;
     request.open("POST",`http://${ip}:5000/login`,true);
     request.setRequestHeader("Content-Type", "application/json");
     request.send(JSON.stringify({pw: document.getElementById('masterkey').value}));
   }
   catch(e) {
    alert("Unable to connect to server");
   }
}

function getInfo(){
    if(request.readyState==4){
        var resp=JSON.parse(request.responseText);
        if(resp['message'] == 'authorized') {
            alert('authorized.. continueing..')
            document.cookie='{"jwt":"' + resp['jwt'] + '"}'
            var MY_TOKEN = resp['jwt'];
            console.log(document.cookie)
            window.location='keys.html'
        } else {
            alert('unauthorized!');
        }
    }
}