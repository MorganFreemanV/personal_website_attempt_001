var current_color = "";
var heights = document.querySelectorAll("tr");
var widths = heights[0].querySelectorAll("span.circle");

for (var j = 0; j < widths.length; j++) {
  widths[j].addEventListener("click", changecontent(widths[j]));
}

function changecontent(width) {
  width.style.color = "blue";
}
