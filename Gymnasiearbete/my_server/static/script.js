function search(inmatning) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let searchItem = JSON.parse(this.responseText);
            if (searchItem == "") document.getElementById("x").innerHTML = "";
            else {
                let s = "";
                for (let j = 0; j < searchItem.length; j++ ) {
                    for (let i = 0; i < searchItem[j].length; i++) {
                        s += "<tr><td>" + searchItem[j][i][1] + "</td></tr>";
                    }
                }
                document.getElementById("x").innerHTML = s;
            }
        }
    };
    xhttp.open("POST", "/search_products_categories", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("inmatning=" + inmatning);
}