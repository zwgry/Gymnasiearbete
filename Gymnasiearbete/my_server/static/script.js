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
            console.log(response);
            let h="";
            for (let i = 0; i < response[0].length; i++) {
                h += "<div class='col mar5'><a href='/product/"+response[0][i].id+"' class='color-product' style='text-decoration: none;'><div class='product'><img class='center' src="+response[1][i].filepath+" alt=''></div><h3>"+response[0][i].name+"</h3></a></div>";
            }
            $("#products").html(h);
        }
    });
};