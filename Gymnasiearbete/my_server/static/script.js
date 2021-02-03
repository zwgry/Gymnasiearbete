function searchFunction(input) {
    $.ajax({
        type: 'POST',
        url: "/search_products_categories",
        data: {
            parameter : input
        },
        dataType: "json",
        success: function(response) {
            console.log(response);
            if (response == "empty"){
                $("#searchDropdownMenu").hide();
                return null;
            }  
            let s = "";
            s += "<h5 class='dropdown-header'>Produkt</h5>";
            for (let j = 0; j < response.length; j++ ) {
                for (let i = 0; i < response[j].length; i++) {
                    s += "<a class='dropdown-item search-text-overflow' href='#'>" + response[j][i][1] + "</a>";
                }
                if (j == 0) {
                s += "<h5 class='dropdown-header'>Kategori</h5>";
                }
            }
            $("#searchDropdownMenu").html(s);
            $("#searchDropdownMenu").show();
        }
    });
};

$(document).ready(function(){
    
    var startSlide = 1;
    showSlides(startSlide);

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
});

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}