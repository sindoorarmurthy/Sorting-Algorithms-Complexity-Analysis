function ShowHideDiv() {
    var chkYes = document.getElementsByName("algorithm");
    var dvtext = document.getElementById("dvtext");
    if (chkYes)
        dvtext.style.display = "block";
    else "none";

}
