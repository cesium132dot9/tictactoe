# 0 is empty
# player 1 is 1: "X"
# player 2 is 2: "O"


class TicTacToe: 
    """A custom object for the game of Tic Tac Toe."""
    board: list[list[str]] 
    current_player: int
    player1: tuple[str, int]
    player2: tuple[str, int]

    def __init__(self, player1name: str, player2name: str) -> None: 
        """Initializes the game of Tic Tac Toe."""
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]
        self.current_player = 1
        self.player1 = player1name, 1
        self.player2 = player2name, 2

    def move(self, row: int, column: int, player: int) -> int: 
        """Making a move on the board."""
        if not self._check_move(row, column, player):
            return -1 # move is invalid 
        else: 
            if player == 1: 
                self.board[row - 1][column - 1] = "X"
            else: 
                self.board[row - 1][column - 1] = "O"
            return 1 # move is valid 

    def _check_move(self, row: int, column: int, player: int) -> bool:
        """Checking if the move is valid. Done by checking if the move is out or range then if a player has already 
        played on that location.
        """
        # checking if the move is out of range
        if row > 3 or column > 3:   
            return False
        # checking if a player has already played on that square
        elif self.board[row - 1][column - 1] == "X" or self.board[row - 1][column - 1] == "O":  
            return False
        elif player != 1 and player != 2: 
            return False 
        else: 
            return True
        
    def win_condition(self) -> bool:
        """Checking if a player has won the game. First checking if there are 3 in a row or column. Then checking the diagonals."""
        # checking rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] in ["X", "O"]:
                return True
        # checking columns
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] in ["X", "O"]:
                return True
        # checking top left to bottom right diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] in ["X", "O"]:
            return True
        # checking top right to bottom left diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] in ["X", "O"]:
            return True
        return False
        
    def switch_player(self) -> None: 
        """Switching the current player."""
        if self.current_player == 1: 
            self.current_player = 2
        else: 
            self.current_player = 1