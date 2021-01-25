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
                    if (response == "") {
                        $("#searchDropdownMenu").html("");
                    } else {
                        let s = "";
                        s += "<h5 class='dropdown-header'>Produkt</h5>";
                        for (let j = 0; j < response.length; j++ ) {
                            for (let i = 0; i < response[j].length; i++) {
                                s += "<a class='dropdown-item' href='#'>" + response[j][i][1] + "</a>";
                            }
                            if (j == 0) {
                            s += "<h5 class='dropdown-header'>Kategori</h5>";
                            }
                        }
                        $("#searchDropdownMenu").html(s);
                    }
            }
        });
    };

function searchDropdown() {
    document.getElementById("searchDropdown").datatoggle;
}