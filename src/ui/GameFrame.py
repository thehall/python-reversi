'''
Created on Sep 4, 2018

@author: Eirik
'''
from tkinter import Frame, Tk, BOTH, N, S, W, E, X, Y
from ui.GameButtons import GameButtons
from ui.ScoreBoard import ScoreBoard
from ui.AiSelect import AiSelect
class GameFrame(object):
    '''
    Base UI class.
    Adds scorearea, gamearea and aiselection to Tk()
    '''
    
    def __init__(self, params, click, on_enter_, on_exit_, start_game):
        self.root = Tk()
        
        self.scoreboard = ScoreBoard(self.root)
        self.scoreboard.pack(fill = Y) 

        self.game_buttons = GameButtons(self.root, click, on_enter_, on_exit_)
        self.game_buttons.pack(fill = BOTH, expand = 8)
        
        self.ai_select = AiSelect(start_game)
        self.ai_select.pack(fill = BOTH)
    
    def start(self):
        self.root.mainloop()
        
    def flip_squares(self, move, color):
        self.game_buttons.flip_squares(move, color)
        
    def update_score(self, black, white, empty):
        self.scoreboard.update_score(black, white, empty)
        
    def reset_board(self):
        self.game_buttons.reset_board()