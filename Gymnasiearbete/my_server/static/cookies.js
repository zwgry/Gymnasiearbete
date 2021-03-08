var currentCookie;
var week = 1000*60*60*24*7;

$(document).ready(function(){

  if (getCookie("acceptCookie") != "true") {
    document.getElementById("accept-cookie").style.display = "block";
  }

});

function startCookie(){
  currentCookie = JSON.parse(getCookie("bag"));
  if (currentCookie != null){
    //Nånging fint med kundvagning
  } else {
    createCookie("bag",'[]',week);
    currentCookie = [];
  }
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
  return null;
}

function getProducts(cookie){
  $.ajax({
    type: 'GET',
    url: "/cookie_products",
    data: {
      data:JSON.stringify(cookie),
    },
    dataType : "json",
    success: (response) => {
      console.log(response);
    }});
}

function addProductToCookie(type,product,ammount){
    currentCookie.push([product,ammount]);
    //console.log(currentCookie);
    createCookie(type,currentCookie,week);
}



function createCookie(type,value,time){
  var d = new Date();
  d.setTime(d.getTime() + time);
  var expires = "expires="+d.toUTCString();
  document.cookie = type+"="+JSON.stringify(value)+";"+expires+";path=/; Secure";  
}

function acceptedCookies(){
  createCookie("acceptCookie", true, week);
  document.getElementById("accept-cookie").style.display = "none";
}

function shoppingCart(){
  let h="";
  for (let i = 0; i < response[0].length; i++) {
      h += "";
  }
  $("#shopping-cart").html(h);
}