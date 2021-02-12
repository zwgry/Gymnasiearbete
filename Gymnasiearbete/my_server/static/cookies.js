function runCookie(){
    setCookie("bag",'{"1":2,"3":1}',1000*60*5)
    //document.cookie = "username=Apa;expires=Fri, 12 Feb 2021 15:21:23 GMT;SameSite=Strict"; 
    //document.cookie = 'bag={"1":2,"3":1};expires=Fri, 12 Feb 2021 15:21:23 GMT;SameSite=Strict'; 
    //Promt the user to accept cookies
    //if  (true){
        // set and get cookies
    //} else{
        //redirect to google.com
    //}
    let jsonProducts = getCookie("bag");
    console.log(jsonProducts)
    let products = JSON.parse(jsonProducts);
}

function getCookie(cname){
    var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

//Ajax funktion som hämtar alla produkter

function setCookie(type,value,time){
    var d = new Date();
    d.setTime(d.getTime() + time);
    var expires = "expires="+d.toUTCString();
    document.cookie = type+"="+value+";"+expires+";SameSite=Strict";    
}