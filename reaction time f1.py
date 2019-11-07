import tkinter as tk
import datetime
import random, time
from threading import Thread,Event

from tkinter import *

class windowclass():

        def __init__(self,master):
                self.master = master
                self.frame = tk.Frame(master)
                self.lbl = Label(master , text = "Reaction Time Game", fg = 'white', font = ('Times New Roman',13), bg = 'darkslategray')
                root.configure(bg='darkslategray')
                self.lbl.pack()
                self.btn = Button(master, text = "Start" , bg = 'lightblue', width = 20, command = self.command)
                self.btn.pack()
                self.frame.pack()

num_of_players = 1#int(input("Number of players: "))
players = [{
        'points':0
        } for i in range(num_of_players)]
rounds = 1#set the number of round

def command(self):
                print ('Starting')

                fields = "Player 1"

                for i in range(0, rounds):
                            print("-"*20 + f"\nIt is now round {i+1}!\n" + "-"*20)
                            for player in players:
                                input(f"It is now {player['name']}'s turn.\nPress enter when ready.")
                                time.sleep(.5)
                                print("Get ready..")
                                time.sleep(random.randint(1,4))
                                then = time.time()
                                t = input("GO!!")
                                reaction_time = time.time()-then
                                print(f"{reaction_time*1000:.0f} ms")
                                player["points"] += reaction_time
                                print("Reaction time: {} seconds".format(time))


root = Tk()

root.title("Reaction Time Game")

root.geometry("350x100")

app = windowclass(root)

root.mainloop()
