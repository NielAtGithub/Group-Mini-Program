from tkinter import *
import os

""" ########################### MAIN MENU ##################################"""

""" Menu def functions """
def run_game_Multiplayer():
    window_menu.destroy()
    os.system('python Game_Play_Multiplayer.py')

def game_quit():
    window_menu.destroy()
    os.system('python Quitting.py')


"""   MENU WINDOW   """
window_menu = Tk()
window_menu.title("Three's and Cross")
window_menu.iconbitmap('Tic-Tac-Toe-Game.ico')
window_menu.geometry('1200x600')
window_menu.resizable(False, False)

"""   MENU WIDGETS   """
# Main Menu Text
Display_Title = Label(window_menu,
              text="THREE'S AND CROSS",
              fg ='black',
              font=('Arial', 50))

# Start Game
Button_Start_Multi = Button(window_menu, text= "Start - Multiplayer", padx=30, fg='black', bg='#73b504', borderwidth=-1,
                            font=('Arial', 20), command= run_game_Multiplayer, activeforeground='black',
                            activebackground='#73b504') #This prevent click button from flashing
Button_Start_Multi_Descript = Label(window_menu, text='Play against other player', font=('Arial', 12))

# Quit Game
Button_quit = Button(window_menu, text= "Quit", padx=113, fg='black', bg='#BF0000', borderwidth=-1, font=('Arial', 20),
                     command= game_quit, activeforeground='black', activebackground='#BF0000')
Button_quit_Descript = Label(window_menu, text='Exit the game', font=('Arial', 12))


# Display Menu Widget
Display_Title.place(anchor= CENTER, relx= .5, rely = .2)
Button_Start_Multi.place(anchor= CENTER, relx= .5, rely = .5)
Button_quit.place(anchor= CENTER, relx= .5, rely = .64)

Button_Start_Multi_Descript.place(anchor= W, relx= .63, rely= .5)
Button_quit_Descript.place(anchor= W, relx= .63, rely= .64)


# Loop in Window_menu
window_menu.mainloop()
