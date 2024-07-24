var headone = document.querySelector("#one");
var headtwo = document.querySelector("#two");
var headthree = document.querySelector("#three");

headone.addEventListener("mouseover", transformerone);
headone.addEventListener("mouseout", transformerone2);
headtwo.addEventListener("click", transformertwo);
headthree.addEventListener("dblclick", transformerthree);

function transformerone() {
  headone.textContent = "Mouse hovering over";
  headone.style.color = "red";
}
function transformerone2() {
  headone.textContent = "Hover over me!";
  headone.style.color = "black";
}
function transformertwo() {
  headtwo.textContent = "I've been clicked!";
  headtwo.style.color = "purple";
}
function transformerthree() {
  headthree.textContent = "I've been double-clicked!";
  headthree.style.color = "blue";
}
