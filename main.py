#introduction
def intro():
    print("Welcome to 4 by 4 Tic Tac Toe!")
    input()
    print("|1|2|3|4|\n""|5|6|7|8|\n""|9|10|11|12|\n""|13|14|15|16|")
    print("Refer to the format above as you play the game.")
    input()
    print("How to Play: Player 1 will be represented by X, and Player 2 will be represented by O. "
          "Each will take turns marking the spaces in a 4*4 grid. The first player to mark 4"
          " in a row either horizontal, veritical, or diagonal will win.")
    input("Press enter to play...")

#gameboard
board = ["" for x in range(16)]
def print_board():
    row1 = "|{}|{}|{}|{}|".format(board[0], board[1], board[2], board[3])
    row2 = "|{}|{}|{}|{}|".format(board[4], board[5], board[6], board[7])
    row3 = "|{}|{}|{}|{}|".format(board[8], board[9], board[10], board[11])
    row4 = "|{}|{}|{}|{}|".format(board[12], board[13], board[14], board[15])

    print(row1)
    print(row2)
    print(row3)
    print(row4)

#player turns
turn = 0
def player_move(icon):
    global turn
    player = (turn % 2) + 1
    if player == 1:
        icon = "X"
    elif player == 2:
        icon = "O"
    print("Your turn player {}" .format(player))
    choice = int(input("Enter your move 1-16:").strip())
    if board[choice-1] == "":
        board[choice-1] = icon
        turn += 1
    elif choice not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16):
        print("Invalid, please try again.")
        input()
    else:
        print("That space is already taken,  please try again.")
        input()
#win
def is_victory(icon):
    victory = False
    if (board[0] == icon and board[1] == icon and board[2] == icon and board[3] == icon):
       victory = True
    elif (board[4] == icon and board[5] == icon and board[6] == icon and board[7] == icon):
       victory = True
    elif (board[8] == icon and board[9] == icon and board[10] == icon and board[11] == icon):
        victory = True
    elif (board[12] == icon and board[13] == icon and board[14] == icon and board[15] == icon):
        victory = True 
    elif (board[0] == icon and board[4] == icon and board[8] == icon and board[12] == icon):
        victory = True
    elif (board[1] == icon and board[5] == icon and board[9] == icon and board[13] == icon):
        victory = True
    elif (board[2] == icon and board[6] == icon and board[10] == icon and board[14] == icon):
        victory = True
    elif (board[3] == icon and board[7] == icon and board[11] == icon and board[15] == icon):
        victory = True
    elif (board[0] == icon and board[5] == icon and board[10] == icon and board[15] == icon):
        victory = True
    elif (board[3] == icon and board[6] == icon and board[9] == icon and board[12] == icon):
        victory = True
    if victory == True:
        return True
    else:
        return False

#tie
def draw():
    if is_victory == False:
        return True
    else:
        return False

#run game
intro()
while True:
    while True:
        print_board()
        player_move("X")
        print_board()
        if is_victory("X"):
            print("Player 1 wins!")
            break
        elif draw():
            print("It's a draw!")
            break
        player_move("O")
        if is_victory("O"):
            print("Player 2 wins!")
            break
        elif draw():
            print("It's a draw!")
            break
    print("Thanks for playing!")
    break
    

        