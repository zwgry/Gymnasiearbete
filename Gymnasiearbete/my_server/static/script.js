function search(inmatning) {
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let searchItem = JSON.parse(this.responseText);
            if (searchItem == "") document.getElementById("list_employees").innerHTML = "";
            else {
                let s = "";
                for (let i = 0; i < employees.length; i++) {
                    s += "<tr><td>" + employees[i][1] + "</td><td>" + employees[i][3] + "</td></tr>";
                }
                document.getElementById("list_employees").innerHTML = s;
            }
        }
    };
    xhttp.open("POST", "/ajax", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("inmatning=" + inmatning);
}