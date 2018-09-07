'''
Created on Sep 4, 2018

@author: Eirik
'''
from tkinter import Frame, Label, E, W, StringVar
class ScoreBoard(Frame):
    '''
    Displaying the current score / status of the game
    '''
    def __init__(self, params):
        super().__init__()
        self.white_text = StringVar(value = "white: 2")
        self.black_text = StringVar(value = "black: 2")
        self.empty_text = StringVar(value = "empty: 60")
        self.status = StringVar(value = "Current player: black")
        l1 = Label(self, textvariable = self.white_text)
        l2 = Label(self, textvariable = self.black_text)
        l3 = Label(self, textvariable = self.empty_text)
        l4 = Label(self, textvariable = self.status)
        
        l1.grid(row = 0, column = 0, columnspan = 1, sticky = (E, W))
        l2.grid(row = 0, column = 1, columnspan = 1)
        l3.grid(row = 0, column = 2, columnspan = 1)
        l4.grid(row = 1, column = 0, columnspan = 3)
        
    def update_status(self, text):
        self.status.set(text)
    
    # Update the stringVars (will update the labels they are attached to)
    def update_score(self, black, white, empty):
        self.black_text.set("black: %s" %black)
        self.white_text.set("white: %s" %white)
        self.empty_text.set("empty: %s" %empty)