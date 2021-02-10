function searchFunction(input) {
    $.ajax({
        type: 'POST',
        url: "/search_products_categories",
        data: {
            parameter : input
        },
        dataType: "json",
        success: function(response) {
            if (response == "empty"){
                $("#searchDropdownMenu").hide();
                return null;
            }  
            let s = "";
            s += "<h5 class='dropdown-header'>Produkt</h5>";
            let id = 1;
            for (let j = 0; j < response.length; j++ ) {
                for (let i = 0; i < response[j].length; i++) {
                    s += "<a class='dropdown-item search-text-overflow' href='#' id='dropdown"+id+"'>" + response[j][i]['name'] + "</a>";
                    id++;
                }
                if (j == 0) {
                s += "<h5 class='dropdown-header'>Kategori</h5>";
                }
            }
            $("#searchDropdownMenu").html(s);
            addHref(response,id);
            $("#searchDropdownMenu").show();
        }
    });
};

function searchDropdown() {
    document.getElementById("searchDropdown").datatoggle;
}

function addHref(response,id){
    let current_id = 1;
    for (let j = 0; j < response.length; j++ ) {
        for (let i = 0; i < response[j].length; i++) {
            var a = document.getElementById("dropdown"+current_id);
            if (j == 0){
                a.href = "/product/"+response[j][i]['id'];
            } else {
                a.href = "/products/"+response[j][i]['id'];
            }
            current_id++;
            if (current_id > id){
                break;
            }
        }
    }
}

function sortASC(category){
    $.ajax({
        type: 'POST',
        url: "/sort",
        data: {
            category : category,
            order : "ASC"
        },
        dataType: "json",
        success: function(response) {
            console.log(response)
            let s = "";
            let id = 1;
            for (let i = 0; i < response.length; i++) {
                s += "<h1>response[i][name]</h1>";
            }
            $("#test").html(s);
        }
    });
};

function sortDSC(category){
    $.ajax({
        type: 'POST',
        url: "/sort",
        data: {
            category : category,
            order : "DSC"
        },
        dataType: "json",
        success: function(response) {
            console.log(response)
            let s = "";
            let id = 1;
            for (let i = 0; i < response.length; i++) {
                s += "<h1>response[i][name]</h1>";
            }
            $("#test").html(s);
        }
    });
};

function sortPOP(category){
    $.ajax({
        type: 'POST',
        url: "/sort",
        data: {
            category : category,
            order : "POP"
        },
        dataType: "json",
        success: function(response) {
            
        }
    });
};

var slideIndex = 1;

$(document).ready(function(){
    
    showSlides(slideIndex);

});

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    var i; 
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");
    if (n > slides.length) {slideIndex = 1}    
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";  
    dots[slideIndex-1].className += " active";
}