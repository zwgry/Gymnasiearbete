var currentCookie;
var week = 1000*60*60*24*7;

$(document).ready(function(){
  startCookie();
  if (getCookie("acceptCookie") != "true") {
    document.getElementById("accept-cookie").style.display = "block";
  }
});

function startCookie(){
  currentCookie = JSON.parse(getCookie("bag"));
  console.log(JSON.parse(getCookie("bag")));
  if (currentCookie != null){
    if (currentCookie == "[]") {
      currentCookie = JSON.parse(currentCookie);
    }
    addProductToCookie("bag",3,3);
  } else {
    console.log("aaaa")
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

function addProductToCookie(type,product,ammount){
    currentCookie.push([product,ammount]);
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
  $.ajax({
    type: 'GET',
    url: "/cookie_products",
    data: {
      data:JSON.stringify(currentCookie),
    },
    dataType : "json",
    success: (response) => {
      let h="";
      var totalPrice = 0;
      for (let i = 0; i < response.length; i++) {
        totalPrice += response[i]['price']*response[i]['stock']
        h+='<a href="/product/"'+response[i]["id"]+'><div class="shopping-cart-box color-cherry shopping-cart-link"><div class="shopping-cart-overflow shopping-cart-name"><p>'+response[i]["name"]+'</p></div><div class="shopping-cart-amount"><p>'+response[i]["stock"]+' st</p></div><div class="shopping-cart-price"><p>'+response[i]["price"]+' kr</p></div></div></a>'
      }
      h+='<div class="shopping-cart-box color-cherry"><div style="float: left; width: 50%;"><p>Totalt: '+totalPrice+' kr</p></div><div style="float: right; width: 50%;"><button type="submit" class="btn btn-cherry">Gå vidare!</button></div></div>'
      $("#shopping-cart").html(h);
    }});
}