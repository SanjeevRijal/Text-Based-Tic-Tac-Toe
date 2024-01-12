
def print_board():
    for rows in board:
        print (rows[0],rows[1],rows[2],rows[3],rows[4])


def update_board(player_sign, player_input):
    # updating board index after each user inputs
    for row in board:
        if player_input in row:
            index_to_update = row.index(player_input)
            row[index_to_update] = player_sign
    print_board()


def winner_checker(player_sign):
    for row in board:
        # this will check if any winner in rows
        if row.count(player_sign) == 3:
            return True


    # making new list of columns
    new_list = []
    for i in range(len(board)):
        new_list.append([row[i] for row in board])

    # this will check if any winner based on column match
    for column_list in new_list:
        if column_list.count(player_sign) == 3:
            return True
        # creating diagnoal list

    diagonal1 = [board[i][i] for i in range(len(board))]
    diagonal2 = [board[i][len(board) - i - 1] for i in range(len(board))]

    # this will check if any winner based on diagonal match

    if diagonal1.count(player_sign) == 3 or diagonal2.count(player_sign) == 3:
        return True

def winner_announcer():
    if player_X > player_O:
        print(f"Computer win.\nPlayer X: {player_X}\nPlayer O: {player_O}")
    elif player_O > player_X:
        print(f"Player win.\nPlayer O: {player_O}\nPlayer X: {player_X}")
    else:
        print(f"It's a tie.\nPlayer X: {player_X}\nPlayer O: {player_O}")

def already_enter_number_checker():
    user_input = input("Type in a number:  ")
    if user_input in already_selected_number:
        print(f"{user_input} is already used, choose another number")
        already_enter_number_checker()
    else:
        return user_input

def turn_counter(turn):
    if turn > 8:
        print("It's a tie.")
        print(f"Current Score\nPlayer X: {player_X}\nPlayer O:{player_O} ")
        return True


already_selected_number = []
player_O = 0
player_X = 0
turn = 0
player_X_sign = "X"
player_O_sign = "O"
while True:
    board = [
        ['1', '|', '2', '|', '3'],
        ['-', '-', '-', '-', '-'],
        ['4', '|', '5', '|', '6'],
        ['-', '-', '-', '-', '-'],
        ['7', '|', '8', '|', '9']
    ]
    print_board()
    while True:
        if not winner_checker(player_X_sign):
            print("\n")
            print("*"*10 + "Player X" + "*"*10)
            user_input = already_enter_number_checker()
            update_board(player_X_sign, user_input)
            already_selected_number.append(user_input)
            turn +=1

        if winner_checker(player_X_sign):
            player_X += 1
            print(f"Current Score\nPlayer X: {player_X}\nPlayer Y:{player_O} ")
            break

        if turn_counter(turn):
            break

        if not winner_checker(player_O_sign):
            print("*" * 10 + "Player O" + "*" * 10)
            user_input = already_enter_number_checker()
            update_board(player_O_sign, user_input)
            already_selected_number.append(user_input)
            turn +=1


        if winner_checker(player_O_sign):
            player_O +=1
            print(f"Current Score\nPlayer X: {player_X}\nPlayer O:{player_O} ")
            break

        if turn_counter(turn):
            break

    play_again = input("Do you want to play again(Y/N):  ")
    if play_again.upper()=="N":
        winner_announcer()
        break
    else:
        already_selected_number=[]
        turn=0


