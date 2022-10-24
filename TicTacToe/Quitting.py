from tkinter import *
import tkinter as tk

""" Quit def functions """
def Quit_Game():
    quit()


"""   QUIT WINDOW   """
Window_Quitting = tk.Tk()
Window_Quitting.title("Tic Tac Toe")
Window_Quitting.iconbitmap('Tic-Tac-Toe-Game.ico')
Window_Quitting.geometry('1200x600')
Window_Quitting.resizable(False, False)


"""   QUIT WIDGETS   """
CreditLeft = Label(text='Project Manager \n \n Business Analyst' + '\n'*4 + 'System Analyst \n \n Programmer' + '\n'*4 + 'Documentation Analyst',
                   bd=1, justify='right', font=('Arial', 12, 'bold'))
CreditLeft.place(anchor=N, relx=.42, rely=.15)

CreditLeft = Label(text='Ian Calano \n \n Sean Febien \n Jet Cabrera' + '\n'*3 + 'Mellysa Mae Feolino \n \n Mark Niel Corre \n Lance Briones' + '\n'*3 + 'Jay Mark Caudilla',
                   bd=1, fg='gray', justify='left', font=('Arial', 12, 'bold'))
CreditLeft.place(anchor=N, relx=.58, rely=.15)

CreditBottom1 = Label(text='TIC TAC TOE', font= ('Arial', 20, 'bold'), fg='black')
CreditBottom1.place(anchor= S, relx= .42, rely = .8)
CreditBottom2 = Label(text='mini project by group two', font= ('Arial', 12, 'bold'), fg='gray')
CreditBottom2.place(anchor= S, relx= .58, rely = .795)


""" Delay Time before quit to see credits """
Window_Quitting.after(5000, Quit_Game) #It last 5 seconds

Window_Quitting.mainloop()




