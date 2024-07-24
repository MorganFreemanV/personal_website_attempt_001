var restart_game = document.querySelector("#restartbtn");

var squares = document.querySelectorAll("td");

var cur_turn = "";

restart_game.addEventListener('click', restartgame);

for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', changecontent);
}

function restartgame() {
    for (var i = 0; i < squares.length; i++) {
        squares[i].textContent = '';
        cur_turn = '';
    }
}

function changecontent() {
    if (cur_turn === '' ||  cur_turn === 'O') {
        this.textContent = 'X';
        cur_turn = 'X';
    } else if (cur_turn === "X") {
        this.textContent = "O";
        cur_turn = "O";
    }
}