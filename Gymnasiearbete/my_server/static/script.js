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
            if (JSON.stringify(response[0]) != '[]'){
                s += "<h5 class='dropdown-header search-text-color color-white'>Produkt</h5>";
            }
            let id = 1;
            for (let j = 0; j < response.length; j++ ) {
                for (let i = 0; i < response[j].length; i++) {
                    if (response[j][i].name != 'Main') {
                        s += "<a class='dropdown-item search-text-overflow search-text-color color-white pl-5' href='#' id='dropdown"+id+"'>" + response[j][i].name + "</a>";
                        id++;
                    }
                }
                if (j == 0) {
                    if (JSON.stringify(response[1]) != '[]' && JSON.stringify(response[1]) != JSON.stringify([{"id":0,"name":"Main","description":"Main","super_category":0}])){
                        s += "<h5 class='dropdown-header search-text-color color-white'>Kategori</h5>";
                    }
                
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

function sort(category, order){
    $.ajax({
        type: 'POST',
        url: "/sort",
        data: {
            category : category,
            order : order
        },
        dataType: "json",
        success: function(response) {
            let h="";
            for (let i = 0; i < response[0].length; i++) {
                for ( var j = 0; j < response[1].length; j++) {
                    if (response[1][j].product_id == response[0][i].id) {
                        var picture = response[1][j];
                    }
                }
                h += "<div class='col mar5'><a href='/product/"+response[0][i].id+"' class='color-text-cherry' style='text-decoration: none;'><div class='product'><img class='center' src=/"+picture.filepath+" alt=''></div><h3>"+response[0][i].name+"</h3><h6>"+response[0][i].price+" kr</h6></a></div>";
            }
            $("#products").html(h);
        }
    });
};