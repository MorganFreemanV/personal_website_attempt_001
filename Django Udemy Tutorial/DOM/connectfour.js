// player 1 prompt, color is blue
var player1 = prompt("What is your name? You will be blue");
$("#player1").text(player1);
var player1color = "rgb(0, 0, 255)";

// player 2 prompt, color is red
var player2 = prompt("What is your name? You will be red");
var player2color = "rgb(255, 0, 0)";
$("#player2").text(player2);

// initiate turn
var turn = 1;
// assign variable table to tr, table rows
table = $("table tr");

// on button click, run the below sequence of code
$("button").on("click", function () {
  // find column number
  var col = $(this).closest("td").index();

  // function to check current player color
  var curplayercolor = checkplayer();

  // function to check row to drop down to
  var row = checkrow(curplayercolor, col);

  // function to drop down color
  addrow(row, col, curplayercolor);
  turn = turn * -1;

  // function to check if connected four
  // function to check wincon
});

function checkplayer() {
  if (turn === 1) return player1color;
  else return player2color;
}

function checkrow(curplayercolor, col) {
  for (var rows = 6; rows > -1; rows--) {
    var colorreport = table
      .eq(rows)
      .find("td")
      .eq(col)
      .find("button")
      .css("background-color");
    if (colorreport === "rgb(255, 228, 196)") {
      return rows;
    }
  }
}

function addrow(row, col, curplayercolor) {
  table
    .eq(row)
    .find("td")
    .eq(col)
    .find("button")
    .css("background-color", curplayercolor);
}
