# 0 is empty
# player 1 is 1: "X"
# player 2 is 2: "O"

# empty board 
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

run_game = True
player = 1
player1_name = ''
player2_name = ''

def turn(row: int, column: int, player: int, board: list[list[int]]) -> bool: 
    if row > 3 or column > 3:  # checking if the move is out of range 
        return False
    elif board[row - 1][column - 1] == 1 or board[row - 1][column - 1] == 2:  # checking if a player has already played on that square
        return False

    # actually inputting the move
    if player == 1: 
        board[row - 1][column - 1] = 1
        return True
    elif player == 2: 
        board[row - 1][column - 1] = 2
        return True
    else: 
        return False


def win_condition(board: list[list[int]]) -> bool:
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 1 or \
            board[i][0] == board[i][1] == board[i][2] == 2:  # checking if there are 3 in a row 
            return True
        if board[0][i] == board[1][i] == board[2][i] == 1 or \
            board[0][i] == board[1][i] == board[2][i] == 2:  # checking if there are 3 in a column 
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
    
    return False
    

turn_so_far = 0

while run_game: 
    move_validity = False

    if turn_so_far == 0: 
        player1_name = input("Please enter your name, player 1: ").upper()
        player2_name = input("Please enter your name, player 2: ").upper()
        turn_so_far += 1

    while not move_validity: 
        if player == 1: 
            row, column = int(input(f"{player1_name}, enter the row you would play in: ")), \
                int(input(f"{player1_name}, enter the column you would like to player in: "))
            move_validity = turn(row, column, player, board)
        elif player == 2: 
            row, column = int(input(f"{player2_name}, enter the row you would play in: ")), \
                int(input(f"{player2_name}, enter the column you would like to player in: "))
            move_validity = turn(row, column, player, board)

    for row in board: 
        print(row)
    
    if win_condition(board):
        if player == 1:  
            print(f"CONGRATS {player1_name} YOU WIN!!!!")
            run_game = False
        else: 
            print(f"CONGRATS {player2_name} YOU WIN!!!!")
            run_game = False

    if turn_so_far == 9 and not win_condition(board): 
        print(f"AWWWWWWW shucks, {player1_name} and {player2_name} you guys drew")
        run_game = False
    
    turn_so_far += 1
    if player == 1: 
        player = 2
    else: 
        player = 1