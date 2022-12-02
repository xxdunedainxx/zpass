console.log("Load core JS file")

function log(){
}

function redirectToHome(ip){
   window.location.href=`http://${ip}:5000/client/html/home.html`
}

function redirectToSetup(ip){
   window.location.href=`http://${ip}:5000/client/html/setup.html`
}