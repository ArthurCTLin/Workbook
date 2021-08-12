# Tic Tac Toe

from tkinter import *
import random

def next_turn(row, col):
    global player
    
    if grid[row][col]["text"] == "" and winner_check() is False:
        if player == symbol[0]:
            grid[row][col]["text"] = player
            if winner_check() is False:
                player = symbol[1]
                label.config(text= (symbol[1]+" turn~"))
            elif winner_check() is True:
                label.config(text=(symbol[0]+" is the winner!"))
            elif winner_check() == "Tie":
                label.config(text="Tie")
        else:
            grid[row][col]["text"] = player
            if winner_check() is False:
                player = symbol[0]
                label.config(text= (symbol[0]+" turn~"))
            elif winner_check() is True:
                label.config(text=(symbol[1]+" is the winner!"))
            elif winner_check() == "Tie":
                label.config(text="Tie")

def winner_check():
    
    for row in range(3):
        if grid[row][0]["text"]==grid[row][1]["text"]==grid[row][2]["text"]!="":
            for i in range(3):
                grid[row][i].config(bg="green")
            return True

    for col in range(3):
        if grid[0][col]["text"]==grid[1][col]["text"]==grid[2][col]["text"]!="":
            for i in range(3):
                grid[i][col].config(bg="green")
            return True
        
    if grid[0][0]["text"]==grid[1][1]["text"]==grid[2][2]["text"]!="":
        for i in range(3):
                grid[i][i].config(bg="green")
        return True

    elif grid[0][2]["text"]==grid[1][1]["text"]==grid[2][0]["text"]!="":
        for i in range(3):
                grid[2-i][i].config(bg="green")
        return True
    
    elif empty_space() is False:
        for row in range(3):
            for col in range(3):
                grid[row][col].config(bg="orange")
        return "Tie"
    
    else:
        return False


def empty_space():
    
    spaces = 9
    for row in range(3):
        for col in range(3):
            if grid[row][col]["text"]!="":
                spaces -= 1
    if spaces==0:
        return False
    else:
        return True

def new_game():
    global player
    
    player = random.choice(symbol)
    label.config(text = player + " turn~")
    
    for row in range(3):
        for col in range(3):
            grid[row][col].config(text="", bg="#F0F0F0")
    

window = Tk()
window.title("Tic Tac Toe")
symbol = ["x", "o"]
player = random.choice(symbol)

grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = Label(text=player+" turn~", font=("consolas", 40))
label.pack(side="top")

restart_button = Button(text="Restart", font=("consolas", 20), command=new_game)
restart_button.pack(side="bottom")

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        grid[row][col] = Button(frame, font=("consolas", 40), width=5, height=2,
                                command=lambda row=row, col=col: next_turn(row, col))
        grid[row][col].grid(row=row, column=col)

window.mainloop()
