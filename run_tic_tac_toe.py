import tic_tac_toe as ttt

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
            move_validity = ttt.turn(row, column, player, board)
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