import random
from random import randint
from tkinter import *


class DiceRoller(object):

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.label = Label(master, font=("times", 200))
        button = Button(master, text="Rolar Dados", command=self.roll)
        button.place(x=200, y=0)

    def roll(self):
        symbols = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
        self.label.config(
            text=f"{random.choice(symbols)}{random.choice(symbols)}")
        self.label.pack()

    """def n(sides):
        return randint(1, sides)

    def roll(n, sides):
        return tuple(n(sides) for _ in range(n))"""


if __name__ == "__main__":
    root = Tk()
    root.title("jogo de dados")
    root.geometry("500x300")
    DiceRoller(root)
    root.mainloop()
    dice = roll(2, 10)
"""print(dice, sum(dice))
# (20, 18, 1) 39"""
