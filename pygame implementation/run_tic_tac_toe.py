import tic_tac_toe as ttt

turn_so_far = 0
run_game = True

# Move game creation outside the loop
player1_name = input("Please enter your name, player 1: ").upper()
player2_name = input("Please enter your name, player 2: ").upper()
game = ttt.TicTacToe(player1_name, player2_name)

while run_game: 
    go_turn = True
    while go_turn: 
        if game.current_player == 1: 
            row, column = int(input(f"{player1_name}, enter the row you would play in: ")), \
                int(input(f"{player1_name}, enter the column you would like to player in: "))
            turn = game.move(row, column, 1)
            if turn == -1: 
                print("INVALID MOVE, PLEASE TRY AGAIN")
            else: 
                go_turn = False
                game.switch_player()
        elif game.current_player == 2: 
            row, column = int(input(f"{player2_name}, enter the row you would play in: ")), \
                int(input(f"{player2_name}, enter the column you would like to player in: "))
            turn = game.move(row, column, 2)
            if turn == -1: 
                print("INVALID MOVE, PLEASE TRY AGAIN")
            else: 
                go_turn = False
                game.switch_player()   

    for row in game.board: 
        print(row)

    if game.win_condition():
        if game.current_player == 1:
            print(f"CONGRATS {player1_name} YOU WIN!!!!")
            run_game = False
        else: 
            print(f"CONGRATS {player2_name} YOU WIN!!!!")
            run_game = False

    if turn_so_far == 8 and not game.win_condition(): 
        print(f"AWWWWWWW shucks, {player1_name} and {player2_name} you guys drew")
        run_game = False
    
    turn_so_far += 1
    