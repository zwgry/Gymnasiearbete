$(document).ready(function(){
    function searchFunction(inmatning) {
        let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                let searchItem = JSON.parse(this.responseText);
                if (searchItem == "") {
                    document.getElementById("searchDropdownMenu").innerHTML = "";
                    searchDropdown();
                } else {
                    searchDropdown();
                    let s = "";
                    s += "<h5 class='dropdown-header'>Produkt</h5>";
                    for (let j = 0; j < searchItem.length; j++ ) {
                        for (let i = 0; i < searchItem[j].length; i++) {
                            s += "<a class='dropdown-item' href='#'>" + searchItem[j][i][1] + "</a>";
                        }
                        s += "<h5 class='dropdown-header'>Kategori</h5>";
                    }
                    document.getElementById("searchDropdownMenu").innerHTML = s;
                }
            }
        };
        xhttp.open("POST", "/search_products_categories", true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("inmatning=" + inmatning);
    });
};

$(document).ready(function() {
    $.ajax({
        type: 'POST',
        url: "/search_products_categories"
        data: {
            inmatning : inmatning
        },
        dataType: "json",
        success: function(response) {

        }
    });
});

function searchDropdown() {
    document.getElementById("searchDropdown").datatoggle;
}