var currentCookie;
var week = 1000*60*60*24*7;

function startCookie(accepted){
  //Promt the user to accept cookies
  createCookie("bag",'[["1","3"],["2","4"]]',week);
  if (accepted){
    currentCookie = JSON.parse(getCookie("bag"));
      if (currentCookie!=null){
        var shoppingBag = getProducts(currentCookie);
        //displayProducts(shoppingBag);
      } else {
        createCookie("bag",'[]',week);
        currentCookie = [];
      }
  } else{
    window.location.replace("https://www.google.com/");
  }
  let jsonProducts = getCookie("bag");
  let products = JSON.parse(jsonProducts);
  addProductToCookie("bag","test",2);
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

//Ajax till servern
function getProducts(cookie){
  //AJAX query
  //return products
}

function addProductToCookie(cookie,product,ammount){
  if (currentCookie == []) {
    currentCookie = [[product,ammount]];
    createCookie("bag",currentCookie,week);
  } else {
    var tempCookie = [];
    for (let i = 0; i < currentCookie.length; i++) {
      console.log(currentCookie[i]);
      
    }
  }
}

function createCookie(type,value,time){
  var d = new Date();
  d.setTime(d.getTime() + time);
  var expires = "expires="+d.toUTCString();
  document.cookie = type+"="+value+";"+expires+";path=/; Secure";  
}