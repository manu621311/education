var modal = document.getElementById("modal");
var span = document.getElementsByClassName("close")[0];
window.onload=function(){
    Modal_disp();
}
function Modal_disp(){
    modal.style.display="block";
}
span.onclick = function() {
    modal.style.display = "none";
  }