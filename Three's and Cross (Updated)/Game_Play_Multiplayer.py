from tkinter import *
import random
import os

""" ########################### IN GAME (Multiplayer) ##################################"""


""" Game def functions """

# Return to menu #######################################################################################################
def Return_Menu():
    window_play.destroy()
    os.system('python MainMenu.py')

# Switch player's turn #################################################################################################
def next_turn(row, column):

    global player
    if buttons[row][column]['text'] == "" and check_winner() is False:

        ### When player currently is 0
        if player == players1v1[0]:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players1v1[1]
                Announce.config(text=(players1v1[1]+"'s Turn"))

            elif check_winner() is True:
                Announce.config(text=(players1v1[0]+" Won"+'\n'+"The Round"))

            elif check_winner() == "Tie":
                Announce.config(text=("Round"+'\n'+"Draw"))

        ### When player currently is 1
        else:
            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players1v1[0]
                Announce.config(text=(players1v1[0]+"'s Turn"))

            elif check_winner() is True:
                Announce.config(text=(players1v1[1]+" Won"+'\n'+"The Round"))

            elif check_winner() == "Tie":
                Announce.config(text=("Round"+'\n'+"Draw"))


# Check for Winning conditions #########################################################################################
def check_winner():

    ### Check for Draw
    if empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='orange')
        return "Tie"

    ### Check for winner by row
    elif buttons[0][0]['text'] == buttons[0][1]['text'] == buttons[0][2]['text'] != "":
        buttons[0][0].config(bg='green')
        buttons[0][1].config(bg='green')
        buttons[0][2].config(bg='green')
        return True
    elif buttons[1][0]['text'] == buttons[1][1]['text'] == buttons[1][2]['text'] != "":
        buttons[1][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[1][2].config(bg='green')
        return True
    elif buttons[2][0]['text'] == buttons[2][1]['text'] == buttons[2][2]['text'] != "":
        buttons[2][0].config(bg='green')
        buttons[2][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True

    ### Check for winner by column
    elif buttons[0][0]['text'] == buttons[1][0]['text'] == buttons[2][0]['text'] != "":
        buttons[0][0].config(bg='green')
        buttons[1][0].config(bg='green')
        buttons[2][0].config(bg='green')
        return True
    elif buttons[0][1]['text'] == buttons[1][1]['text'] == buttons[2][1]['text'] != "":
        buttons[0][1].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][1].config(bg='green')
        return True
    elif buttons[0][2]['text'] == buttons[1][2]['text'] == buttons[2][2]['text'] != "":
        buttons[0][2].config(bg='green')
        buttons[1][2].config(bg='green')
        buttons[2][2].config(bg='green')
        return True

    ### Check for winner by diagonal
    elif buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][2].config(bg='green')
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg='green')
        buttons[1][1].config(bg='green')
        buttons[2][0].config(bg='green')
        return True

    ### Proceed to next_turn (if winning condition is not meet)
    else:
        return False


# Declare Tie ##########################################################################################################
def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False


# Restart game #########################################################################################################
def new_game():
    global player

    player = random.choice(players1v1)
    Announce.config(text=player + "'s Turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="white")


########################################################################################################################

"""   Creating Gameplay Window   """
window_play = Tk()
window_play.title("Three's and Cross")
window_play.iconbitmap('Tic-Tac-Toe-Game.ico')
window_play.geometry('1200x600')
window_play.resizable(False, False)


""" Game 'Multiplayer' Functions (for Player vs Player)  """

# Players
players1v1 = ["X","O"]
player = random.choice(players1v1)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]


""" In-Game Widgets """

Announce = Label(window_play, anchor=N, text= player + "'s Turn", font=("arial", 30), justify=RIGHT)
Announce.place(anchor=E, relx=.98, rely=.87)

# Back to menu button
Return_menu_Button = Button(window_play, text= "Return Menu", font=('Arial', 20), bg='#BF0000', borderwidth=-1, padx=7,
                            command= Return_Menu, activeforeground='black', activebackground='#BF0000')
Return_menu_Button.place(anchor=CENTER, relx=.1, rely=.88)

# Reset button
reset_button = Button(window_play, text= "Restart Game", font=('Arial', 20), bg='#CC5500', borderwidth=-1,
                      command= new_game, activeforeground='black', activebackground='#CC5500')
reset_button.place(anchor=CENTER, relx=.1, rely=.78)


GameBoard = Frame(window_play)
GameBoard.place(anchor=CENTER, relx=.5, rely=.5)
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(GameBoard, text="", font=("arial", 40, "bold"), bg = 'white',
                                      activebackground='white', width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column), borderwidth=-1)
        buttons[row][column].grid(row=row, column=column, padx=2, pady=2)


# Loop in Window_Play
window_play.mainloop()
