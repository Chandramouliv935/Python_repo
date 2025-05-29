import tkinter

def set_title(row, column):
    global curr_player, turns

    if game_over:
        return
    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = curr_player
    turns += 1

    if curr_player == playero:
        curr_player = playerx
    else:
        curr_player = playero

    label["text"] = curr_player + "'s turn"
    check_winner()

def check_winner():
    global game_over

    # Check rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]) and board[row][0]["text"] != "":
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_grey)
            game_over = True
            return

    # Check columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]) and board[0][column]["text"] != "":
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow, background=color_light_grey)
            game_over = True
            return

    # Check diagonals
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]) and board[0][0]["text"] != "":
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_grey)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]) and board[0][2]["text"] != "":
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_grey)
        board[1][1].config(foreground=color_yellow, background=color_light_grey)
        board[2][0].config(foreground=color_yellow, background=color_light_grey)
        game_over = True
        return

    # Check for tie
    if turns == 9:
        game_over = True
        label.config(text="Tie!", foreground=color_yellow)

def new_game():
    global curr_player, turns, game_over
    curr_player = playerx
    turns = 0
    game_over = False
    label.config(text=curr_player + "'s turn", foreground="white")
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", foreground=color_blue, background=color_grey)


playerx = "X"
playero = "O"
curr_player = playerx
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#1017b6"
color_yellow = "#dfe70d"
color_grey = "#3a3a3a"
color_light_grey = "#c3bdbd"

turns = 0
game_over = False

window = tkinter.Tk()
window.title("TIC TAC TOE")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("consolas", 20), background=color_grey, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("consolas", 50, "bold"), 
                                          background=color_grey, foreground=color_blue, width=4, height=1,
                                          command=lambda row=row, column=column: set_title(row, column))
        board[row][column].grid(row=row+1, column=column)

button = tkinter.Button(frame, text="RESTART", font=("Consolas", 20), background=color_grey, foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()
window.mainloop()