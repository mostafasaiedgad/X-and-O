import tkinter as tk
from tkinter import *
import random

main_window = Tk()
main_window.geometry('400x520+340+100')
main_window.resizable(False, False)
main_window.title('X O')
icon = tk.PhotoImage(file=r"D:\MSA\Python Projects\X & O game\photos\game.png")
main_window.iconphoto(False, icon)

players = ["x", "o"]
player = random.choice(players)
game_buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def next_turn(row, col):
    global player
    if game_buttons[row][col]['text'] == '' and check_winner() is False:
        if player == players[0]:
            game_buttons[row][col]['text'] = player

            if check_winner() is False:
                player = players[1]
                main_label.config(text=player + " turn")

            elif check_winner() is True:
                player = players[0]
                main_label.config(text=player + " wins")

            elif check_winner() == "tie":
                main_label.config(text="tie!")

        else:
            game_buttons[row][col]['text'] = player

            if check_winner() is False:
                player = players[0]
                main_label.config(text=player + " turn")

            elif check_winner() is True:
                player = players[1]
                main_label.config(text=player + " wins")

            elif check_winner() == "tie":
                main_label.config(text="tie!")
            

def check_winner():
    for row in range(3):
        if game_buttons[row][0]['text'] == game_buttons[row][1]['text'] == game_buttons[row][2]['text'] != '':
            game_buttons[row][0].config(bg="green")
            game_buttons[row][1].config(bg="green")
            game_buttons[row][2].config(bg="green")
            return True
        
    for col in range(3):
        if game_buttons[0][col]['text'] == game_buttons[1][col]['text'] == game_buttons[2][col]['text'] != '':
            game_buttons[0][col].config(bg="green")
            game_buttons[1][col].config(bg="green")
            game_buttons[2][col].config(bg="green")
            return True  
        
    if game_buttons[0][0]['text'] == game_buttons[1][1]['text'] == game_buttons[2][2]['text'] != '':
        game_buttons[0][0].config(bg="green")
        game_buttons[1][1].config(bg="green")
        game_buttons[2][2].config(bg="green")
        return True      
    
    elif game_buttons[0][2]['text'] == game_buttons[1][1]['text'] == game_buttons[2][0]['text'] != '':
        game_buttons[0][2].config(bg="green")
        game_buttons[1][1].config(bg="green")
        game_buttons[2][0].config(bg="green")
        return True  
    
    elif empty_spaces() is False:
        for row in range(3):
            for col in range(3):
                game_buttons[row][col].config(bg="red")
        return "tie"
    
    else:
        return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if game_buttons[row][col]['text'] != '':
                spaces -= 1

    if spaces == 0:
        return False
    
    else:
        return True

def start_new_game():
    global player
    player = random.choice(players)
    main_label.config(text=player + " turn")
    for row in range(3):
        for col in range(3):
            game_buttons[row][col]['text'] = ''
            game_buttons[row][col].config(bg="#F0F0F0")

main_label = Label(main_window, text=player + " turn", font=("Algerian", 26))
main_label.pack(side='top')

restart_button = Button(main_window, text="Restart", font=("Algerian", 15), bg="#66CD00", command=start_new_game)
restart_button.pack(side='top')

frame = Frame(main_window)
frame.place(x=48, y=100)

for row in range(3):
    for col in range(3):
        game_buttons[row][col] = Button(frame, text="", font=("family", 30), width=4, height=2,
                                        command=lambda row=row, col=col: next_turn(row, col))
        game_buttons[row][col].grid(row=row, column=col)

main_window.mainloop()

