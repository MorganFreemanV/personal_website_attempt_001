var current_color = "";
var height = document.querySelectorAll("tr");
var widths = document.querySelectorAll(".circle");
var turn = 1;

for (var j = 0; j < widths.length; j++) {
  for (var i = 0; i < widths.length; i++) {
    widths[i].addEventListener("click", changecontent);
  }
}

function changecontent() {
  rowind = this.closest("tr").rowIndex;
  colind = this.parentElement.cellIndex;
  for (var i = 6; i > -1; i--) {
    placeholder = document.getElementById("tr").rows[rowind].cells[colind];
    console.log(placeholder);
    if (widths[rowind][colind].style.backgroundColor === "bisque") {
      if (turn === 1) {
        this.style.backgroundColor = "blue";
      } else {
        this.style.backgroundColor = "red";
      }
    }
    turn = turn * -1;
  }
}
