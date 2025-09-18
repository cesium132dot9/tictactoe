class TicTacToe {
    constructor(player1Name, player2Name) {
        this.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ];
        this.currentPlayer = 1;
        this.player1 = [player1Name, 1];
        this.player2 = [player2Name, 2];
        this.gameOver = false;
        this.winner = null;
    }

    move(row, column, player) {
        if (!this._checkMove(row, column, player)) {
            return -1; // invalid move
        } else {
            if (player === 1) {
                this.board[row][column] = "X";
            } else {
                this.board[row][column] = "O";
            }
            return 1; // valid move
        }
    }

    _checkMove(row, column, player) {
        // checking if the move is out of range
        if (row > 2 || column > 2 || row < 0 || column < 0) {
            return false;
        }
        // checking if a player has already played on that square
        if (this.board[row][column] === "X" || this.board[row][column] === "O") {
            return false;
        }
        if (player !== 1 && player !== 2) {
            return false;
        }
        return true;
    }

    winCondition() {
        // checking rows
        for (let i = 0; i < 3; i++) {
            if (this.board[i][0] === this.board[i][1] && 
                this.board[i][1] === this.board[i][2] && 
                (this.board[i][0] === "X" || this.board[i][0] === "O")) {
                return true;
            }
        }
        
        // checking columns
        for (let i = 0; i < 3; i++) {
            if (this.board[0][i] === this.board[1][i] && 
                this.board[1][i] === this.board[2][i] && 
                (this.board[0][i] === "X" || this.board[0][i] === "O")) {
                return true;
            }
        }
        
        // checking top left to bottom right diagonal
        if (this.board[0][0] === this.board[1][1] && 
            this.board[1][1] === this.board[2][2] && 
            (this.board[0][0] === "X" || this.board[0][0] === "O")) {
            return true;
        }
        
        // checking top right to bottom left diagonal
        if (this.board[0][2] === this.board[1][1] && 
            this.board[1][1] === this.board[2][0] && 
            (this.board[0][2] === "X" || this.board[0][2] === "O")) {
            return true;
        }
        
        return false;
    }

    switchPlayer() {
        if (this.currentPlayer === 1) {
            this.currentPlayer = 2;
        } else {
            this.currentPlayer = 1;
        }
    }

    isBoardFull() {
        for (let row of this.board) {
            for (let cell of row) {
                if (cell === "") {
                    return false;
                }
            }
        }
        return true;
    }
}

let game;

function startGame() {
    const player1Name = document.getElementById('player1Input').value.trim() || 'Player 1';
    const player2Name = document.getElementById('player2Input').value.trim() || 'Player 2';
    
    game = new TicTacToe(player1Name, player2Name);
    
    document.getElementById('playerSetup').style.display = 'none';
    document.getElementById('gameArea').style.display = 'block';
    
    updateStatus();
    updateBoard();
}

function makeMove(row, col) {
    if (game.gameOver) return;
    
    const result = game.move(row, col, game.currentPlayer);
    
    if (result !== -1) { // Valid move
        updateBoard();
        
        if (game.winCondition()) {
            game.gameOver = true;
            game.winner = game.currentPlayer === 1 ? 'X' : 'O';
            showWinner();
        } else if (game.isBoardFull()) {
            game.gameOver = true;
            showDraw();
        } else {
            game.switchPlayer();
            updateStatus();
        }
    }
}

function updateBoard() {
    const cells = document.querySelectorAll('.cell');
    let cellIndex = 0;
    
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            const cell = cells[cellIndex];
            const value = game.board[row][col];
            
            cell.textContent = value;
            cell.className = 'cell';
            
            if (value !== "") {
                cell.classList.add('filled');
                if (value === 'X') {
                    cell.classList.add('x');
                } else {
                    cell.classList.add('o');
                }
            }
            
            cellIndex++;
        }
    }
}

function updateStatus() {
    const status = document.getElementById('status');
    const currentPlayerName = game.currentPlayer === 1 ? game.player1[0] : game.player2[0];
    const symbol = game.currentPlayer === 1 ? 'X' : 'O';
    
    status.innerHTML = `<div class="player-turn">${currentPlayerName}'s turn (${symbol})</div>`;
}

function showWinner() {
    const status = document.getElementById('status');
    const winnerName = game.currentPlayer === 1 ? game.player1[0] : game.player2[0];
    
    status.innerHTML = `<div class="winner-announcement">🎉 ${winnerName} Wins! 🎉</div>`;
}

function showDraw() {
    const status = document.getElementById('status');
    status.innerHTML = `<div class="draw-announcement">🤝 It's a Draw! 🤝</div>`;
}

function restartGame() {
    const player1Name = game.player1[0];
    const player2Name = game.player2[0];
    
    game = new TicTacToe(player1Name, player2Name);
    updateBoard();
    updateStatus();
}

// Allow Enter key to start game
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('player1Input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            document.getElementById('player2Input').focus();
        }
    });
    
    document.getElementById('player2Input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            startGame();
        }
    });
});