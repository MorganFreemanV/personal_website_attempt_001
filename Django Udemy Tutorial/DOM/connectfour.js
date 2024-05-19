var player1 = prompt("What is your name? You will be blue");
$("#player1").attr("id", player1);
var player1color = "blue";
var player2 = prompt("What is your name? You will be red");
var player2color = "red";
$("#player2").attr("id", player2);
var turn = 1;

$("button").on("click", function () {
  var col = $(this).closest("td").index();
  var row = $(this).closest("tr").index();
  var curplayer = checkplayer();
  // function to check player
  // function to check row  to drop down to
  // function to check connectfour
  // function to check wincon
  console.log("col number is: " + col);
  console.log("row number is: " + row);
});

function checkplayer() {
  if (turn === 1) return player1;
  else return player2;
}
