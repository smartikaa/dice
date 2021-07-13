import random
import tkinter as tk
from tkinter import font as tkFont
r = tk.Tk()
helv36 = tkFont.Font(family='Arial', size=36, weight=tkFont.BOLD)
r.geometry("700x450")
r.configure(bg="#0C0F38")
r.title('Dice')
diceLabel=tk.Label(r,text="",font=("times",200),fg="#F8EEEE",bg="#0C0F38")
n=[]
n.append('\u2681')
def roll():
    num=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    n.append(random.choice(num))
    i=len(n)-1
    if n[i] != n[i-1]:
        diceLabel.config(text=n[i])
        diceLabel.pack()
    else:
        roll()



    

button = tk.Button(r, text='ROLL IT!', width=250, command=roll, bg="#EE8D25",font=helv36)
button.pack()
r.mainloop()