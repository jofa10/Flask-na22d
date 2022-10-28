function myFunction() {
  // Get the text field
  var copyText = localStorage.getItem("kod");

  navigator.clipboard.writeText(copyText);

  // Alert the copied text
  document.getElementById("kopiera").innerHTML = "Kopierat!";
}
function changevalue(){


  var kod = prompt("Schemakod", "");
  if (kod != null) {
    document.getElementById("result").innerHTML = kod;
    localStorage.setItem("kod", kod);
}}