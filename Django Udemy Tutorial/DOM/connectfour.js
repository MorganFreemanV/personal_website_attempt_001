// player 1 prompt, color is blue
var player1 = prompt("What is your name? You will be blue");
if (player1) {
  $("#player1").text(player1);
}
var player1color = "rgb(0, 0, 255)";

// player 2 prompt, color is red
var player2 = prompt("What is your name? You will be red");
var player2color = "rgb(255, 0, 0)";
if (player2) {
  $("#player2").text(player2);
}

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

  // function to check if connected four
  if (checkhorizontal() || checkvertical() || checkdiagonal()) {
    restartgame();
  }
  turn = turn * -1;
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

function returncolor(row, col) {
  return table
    .eq(row)
    .find("td")
    .eq(col)
    .find("button")
    .css("background-color");
}

function colormatchcheck(one, two, three, four) {
  return (
    one === two &&
    one === three &&
    one === four &&
    one != "rgb(255, 228, 196)" &&
    one != undefined
  );
}

// check horizontal wins
function checkhorizontal() {
  for (var row = 0; row < 7; row++) {
    for (var col = 0; col < 6; col++) {
      if (
        colormatchcheck(
          returncolor(row, col),
          returncolor(row, col + 1),
          returncolor(row, col + 2),
          returncolor(row, col + 3)
        )
      ) {
        reportwin(turn);
        return true;
      } else {
        continue;
      }
    }
  }
}

// check vertical wins
function checkvertical() {
  for (var col = 0; col < 6; col++) {
    for (var row = 0; row < 7; row++) {
      if (
        colormatchcheck(
          returncolor(row, col),
          returncolor(row + 1, col),
          returncolor(row + 2, col),
          returncolor(row + 3, col)
        )
      ) {
        reportwin(turn);
        return true;
      } else {
        continue;
      }
    }
  }
}

function checkdiagonal() {
  for (var col = 0; col < 6; col++) {
    for (var row = 0; row < 7; row++) {
      if (
        colormatchcheck(
          returncolor(row, col),
          returncolor(row + 1, col + 1),
          returncolor(row + 2, col + 2),
          returncolor(row + 3, col + 3)
        )
      ) {
        reportwin(turn);
        return true;
      } else if (
        colormatchcheck(
          returncolor(row, col),
          returncolor(row - 1, col + 1),
          returncolor(row - 2, col + 2),
          returncolor(row - 3, col + 3)
        )
      ) {
        reportwin(turn);
        return true;
      } else {
        continue;
      }
    }
  }
}

/* function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
} */

function reportwin(turn) {
  if (turn === 1) {
    alert($("#player1").text() + " wins!");
  } else {
    alert($("#player2").text() + " wins!");
  }
  // restartgame();
}

function restartgame() {
  document.location.reload();
}
