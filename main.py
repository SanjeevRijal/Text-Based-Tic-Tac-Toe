
player_score = 0
computer_score= 0
restart_game = 1

def print_board():
    for rows in board:
        print (rows[0],rows[1],rows[2],rows[3],rows[4])


def update_board(player_sign, user_input):
    # updating board index after each user inputs
    for row in board:
        if user_input in row:
            index_to_update = row.index(user_input)
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
    if computer_score > player_score:
        print(f"Computer win.\nComputer Score: {computer_score}\nPlayer Score: {player_score}")
    elif player_score > computer_score:
        print(f"Player win.\nPlayer Score: {player_score}\nComputer Score: {computer_score}")
    else:
        print(f"It's a tie.\nComputer Score: {computer_score}\nPlayer Score: {player_score}")





already_entered_list = []
computer_sing = "X"
user_sign = "O"
while restart_game == 1:
    board = [
        ['1', '|', '2', '|', '3'],
        ['-', '-', '-', '-', '-'],
        ['4', '|', '5', '|', '6'],
        ['-', '-', '-', '-', '-'],
        ['7', '|', '8', '|', '9']
    ]
    print_board()
    while True:
        if not winner_checker(computer_sing):
            print("\n")
            print("*"*10 + "Computer Turn" + "*"*10)
            user_input = input("Type in a number:  ")
            update_board(computer_sing, user_input)

        if winner_checker(computer_sing):
            computer_score+=1
            print(f"Current Score\nComputer Score: {computer_score}\nUser Score:{player_score} ")
            play_again = input("Do you want to play again(Y/N : ")
            if play_again == "Y":
                restart_game = 1
                break
            if play_again =="N":
                winner_announcer()
                restart_game = 6
                break

        if restart_game==1:

            if not winner_checker(user_sign):
                print("*" * 10 + "Player Turn" + "*" * 10)
                user_input = input("Type in a number:  ")
                update_board(user_sign, user_input)

            if winner_checker(user_sign):
                player_score +=1
                print(f"Current Score\nComputer Score: {computer_score}\nUser Score:{player_score} ")
                play_again= input("Do you want to play again(Y/N) : ")
                if play_again == "Y":
                    restart_game =1
                    break
                else:
                    restart_game = 2
                    winner_announcer()
                    break









