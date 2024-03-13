var restart_game = document.querySelector("#restartbtn");

var squares = document.querySelectorAll("td");

restart_game.addEventListener('click', restartgame);

for (var i = 0; i < squares.length; i++) {
    squares[i].addEventListener('click', changecontent);
}

function restartgame() {
    for (var i = 0; i < squares.length; i++) {
        squares[i].textContent = '';
    }
}

function changecontent() {
    if (this.textContent === '') {
        this.textContent = 'X';
    } else if (this.textContent === "X") {
        this.textContent = "O";
    } else {
        this.textContent = "";
    }
}