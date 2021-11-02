from random import *
import time
from tkinter import *


class DiceRoller(object):

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.label = Label(master, font=("times", 200))
        button = Button(master, text="Rolar Dados", command=self.roll)
        button.place(x=200, y=0)


print('-='*20)
print('vou rolar um dado de 20 e mostrarei o resultado do teste')
print('-='*20)
time.sleep(3)
resultado = randint(0, 20)

if resultado <= 1:
    print("Você tirou {} no dado".format(resultado))
    print("Você tirou um DESASTRE")

elif resultado <= 9:
    print("Você tirou {} no dado".format(resultado))
    print("Você tirou um fracasso")

elif resultado <= 15:
    print("Você tirou {} no dado".format(resultado))
    print('Você tirou um sucesso normal')

elif resultado <= 18:
    print("Você tirou {} no dado".format(resultado))
    print('Você tirou um sucesso normal')

else:
    print("Você tirou {} no dado".format(resultado))
    print("Você tirou um sucesso EXTREMO")


def roll(self):
    symbols = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
    self.label.config(
        text=f"{random.choice(symbols)}{random.choice(symbols)}")
    self.label.pack()


if __name__ == "__main__":
    root = Tk()
    root.title("jogo de dados")
    root.geometry("500x300")
    DiceRoller(root)
    root.mainloop()
    dice = roll(2, 10)
