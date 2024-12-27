# 0 is empty
# player 1 is 1: "X"
# player 2 is 2: "O"


class TicTacToe: 
    """A custom object for the game of Tic Tac Toe."""
    board: list[list[int]] 
    current_player: int
    player1: tuple[str, int]
    player2: tuple[str, int]

    def __init__(self, player1name: str, player2name: str) -> None: 
        """Initializes the game of Tic Tac Toe."""
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.current_player = 1
        self.player1 = player1name, 1
        self.player2 = player2name, 2

    def move(self, board: list[list[int]], row: int, column: int, player: int) -> None: 
        """Making a move on the board."""
        if player == 1: 
            board[row - 1][column - 1] = 1
        elif player == 2: 
            board[row - 1][column - 1] = 2
        else: 
            return False
        
    def check_move(self, row: int, column: int, board: list[list[int]]) -> bool:
        """Checking if the move is valid. Done by checking if the move is out or range then if a player has already 
        played on that location.
        """
        # checking if the move is out of range
        if row > 3 or column > 3:   
            return False
        # checking if a player has already played on that square
        elif board[row - 1][column - 1] == 1 or board[row - 1][column - 1] == 2:  
            return False

    def win_condition(self, board: list[list[int]]) -> bool:
        """Checking if a player has won the game. First checking if there are 3 in a row or column. Then checking the diagonals."""
        # checking rows and columns 
        for i in range(3):
            # checking if there are 3 in a row
            if board[i][0] == board[i][1] == board[i][2] == 1 or \
                board[i][0] == board[i][1] == board[i][2] == 2:   
                return True
            # checking if there are 3 in a column
            if board[0][i] == board[1][i] == board[2][i] == 1 or \
                board[0][i] == board[1][i] == board[2][i] == 2:  
                return True 
            
        # checking diagonals
        # checking top left to bottom right 
        if board[0][0] == board[1][1] == board[2][2] == 1 or \
            board[0][0] == board[1][1] == board[2][2] == 2: 
            return True 
        # checking top right to bottom left 
        elif board[0][2] == board[1][1] == board[2][0] == 1 or \
            board[0][2] == board[1][1] == board[2][0] == 2: 
            return True
        
        # if no player has won 
        return False