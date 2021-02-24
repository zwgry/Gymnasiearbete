const { response } = require("express");

var currentCookie;
var week = 1000*60*60*24*7;

function startCookie(accepted){
  //Promt the user to accept cookies
  createCookie("bag",[[1,3],[2,4]],week);
  if (accepted){
    currentCookie = JSON.parse(getCookie("bag"));
    console.log(currentCookie);
      if (currentCookie!=null){
        //var shoppingBag = getProducts(currentCookie);
        //displayProducts(shoppingBag);
      } else {
        createCookie("bag",'[]',week);
        currentCookie = [];
      }
  } else{
    window.location.replace("https://www.google.com/");
  }
  //addProductToCookie("bag",3,2);
  getProducts(currentCookie);
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
