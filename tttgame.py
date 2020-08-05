def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("-----")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-----")
    print(board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker = ''
    while marker != "X" and marker != "O":
        marker = input("Player1 choose X or O: ")
        if marker != "X" and marker !="O" :
            print("WRONG INPUT.YOU CAN ONLY CHOOSE X OR O !")
    
        player1 = marker

        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = "X"
    print(player1,player2)

