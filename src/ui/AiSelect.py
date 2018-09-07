'''
Created on Sep 5, 2018

@author: Eirik
'''
from tkinter import Frame, Label, Button, SUNKEN, RAISED
class AiSelect(Frame):
    '''
    Frame containing buttons to select AI difficulty
    Gets passed start_game which is a function in Controller.
    Clicking a selector button sets it as SUNKEN,
     while setting the others as RAISED
    '''


    def __init__(self, start_game):
        super().__init__()
        self.player1 = 0
        self.player2 = 0
        
        player1_select = Label(self, text = "Player 1")
        player1_select.grid(row = 0, column = 0)
        player2_select = Label(self, text = "Player 2")
        player2_select.grid(row = 1, column = 0)
        
        player1_human = Button(self, text = "Human", command = lambda: self.click(1, 0), relief = SUNKEN)
        player1_human.grid(row = 0, column = 1)
        player1_easy = Button(self, text = "Easy", command = lambda: self.click(1, 1))
        player1_easy.grid(row = 0, column = 2)
        player1_medium = Button(self, text = "Medium", command = lambda: self.click(1, 2))
        player1_medium.grid(row = 0, column = 3)
        player1_hard = Button(self, text = "Hard", command = lambda: self.click(1, 3))
        player1_hard.grid(row = 0, column = 4)
        self.player1_buttons = [player1_human, player1_easy, player1_medium, player1_hard]
        player2_human = Button(self, text = "Human", command = lambda: self.click(2, 0), relief = SUNKEN)
        player2_human.grid(row = 1, column = 1)
        player2_easy = Button(self, text = "Easy", command = lambda: self.click(2, 1))
        player2_easy.grid(row = 1, column = 2)
        player2_medium = Button(self, text = "Medium", command = lambda: self.click(2, 2))
        player2_medium.grid(row = 1, column = 3)
        player2_hard = Button(self, text = "Hard", command = lambda: self.click(2, 3))
        player2_hard.grid(row = 1, column = 4)
        self.player2_buttons = [player2_human, player2_easy, player2_medium, player2_hard]
        start_new_game = Button(self, text = "Start new game!", command = lambda: start_game(self.player1, self.player2))
        start_new_game.grid(row = 2, column = 0)
        
    def click(self, player, level):
        if player == 1:
            self.player1_buttons[self.player1].configure(relief = RAISED)
            self.player1_buttons[level].configure(relief = SUNKEN)
            self.player1 = level
        if player == 2:
            self.player2_buttons[self.player2].configure(relief = RAISED)
            self.player2_buttons[level].configure(relief = SUNKEN)
            self.player2 = level
            