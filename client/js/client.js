console.log('MAIN CLIENT LOADED')
console.log(document.cookie)

var JWT = {}

if(document.cookie != '') {
 JWT = JSON.parse(document.cookie)
}

function submitMasterkey() {
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
     request.open("POST","http://localhost:5000/login",true);
     request.setRequestHeader("Content-Type", "application/json");
     request.send(JSON.stringify({pw: document.getElementById('masterkey').value}));
   }
   catch(e) {
    alert("Unable to connect to server");
   }
}
// curl http://127.0.0.1:5000/update_pws -X POST
//--data '{"key":"test2", "value":"somethingblah"}' -H '
// Content-Type: application/json'
// -H 'X-Authentication: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTE5NzY2NzMsImlhdCI6MTYxMTM3MTg3MywidHlwZSI6ImNsaWVudCJ9.mLYE62sdhpsNnCMtqaQIrTffhfxMw_YG7c48p_DWGMA'

function fetchKeys() {
  if(JWT == '') {
    alert('you need to authenticate')
    window.location('home.html')
  }


  if(window.XMLHttpRequest){
    request=new XMLHttpRequest();
   }
   else if(window.ActiveXObject){
    request=new ActiveXObject("Microsoft.XMLHTTP");
   }

   try  {
     console.log('preparing request')
     request.onreadystatechange=renderKeys;
     request.open("GET","http://localhost:5000/get_pws",true);
     request.setRequestHeader("Content-Type", "application/json");
     request.setRequestHeader("X-Authentication", JWT['jwt']);
     request.send();
   }
   catch(e) {
    alert('something went wrong');
   }
}

function renderKeys(){
    if(request.readyState == 4) {
    if(request.status == 401) {
        alert('unauthorized, redirecting')
        window.location='home.html'
    }
    console.log('request complete?')
        var resp=JSON.parse(request.responseText);
        console.log(resp)
        JWT['keys'] = resp
        keysToHTML()
    }
}

function keysToHTML() {
  var htmlBuilder = "Keys: <br/>"
  for (const [key, value] of Object.entries(JWT['keys'])) {
    console.log(key)
    console.log(value)
    htmlBuilder+=("<div id=\"" + key + "\"><input value=\"" + key + "\"" + "placeholder=\"" + key +  "\">=<input value=\"" + value + "\" placeholder=\"" + value +  "\"> </div>")
   }
   htmlBuilder+="<div id=\"newEntry\"><input value=\"newEntryKey\" placeholder=\"newEntry\">=<input value\"newEntryValue\" placeholder=\"newEntry\"></div>"
   console.log(htmlBuilder)
   document.getElementById('keys').innerHTML=htmlBuilder
}

function postDumpKeys(){
    if(request.readyState == 4) {
        console.log('request complete?')
        var resp=JSON.parse(request.responseText);

        if(request.status != 200) {
            if(request.status == 401) {
                alert('Unauthoried, redirecting to login page')
                window.location='home.html'
            }  else {
                alert('Something went wrong..')
                location.reload()
            }
        }

        if(resp['message'] == 'db updated'){
            console.log(request.responseText)
            alert(resp['message'])
            location.reload()
        } else {
            alert(("Something went wrong... " + resp['message']))
        }
    }
}

function submitKeys(){
    var postBuilder = {}
    var keys = document.getElementById('keys')
    for(var i = 0; i < keys.children.length; i++) {
        console.log(keys.children[i])
        if(keys.children[i].tagName == 'DIV') {
            var key = keys.children[i].children[0].value
            var value = keys.children[i].children[1].value
            if(key == 'newEntryKey') {
                continue;
            } else {
               postBuilder[key] = value
            }
        }
    }
      if(window.XMLHttpRequest){
    request=new XMLHttpRequest();
   }
   else if(window.ActiveXObject){
    request=new ActiveXObject("Microsoft.XMLHTTP");
   }

   try  {
     console.log('preparing dump key request request')
     request.onreadystatechange=postDumpKeys;
     request.open("POST","http://localhost:5000/dump_keys",true);
     request.setRequestHeader("Content-Type", "application/json");
     request.setRequestHeader("X-Authentication", JWT['jwt'])
     request.send(JSON.stringify(postBuilder));
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