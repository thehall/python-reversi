'''
Created on Sep 4, 2018

@author: Eirik
'''
from tkinter import Frame, Button, N, S, W, E, BOTH
from ui.GameButton import GameButton
class GameButtons(Frame):
    '''
    Main UI area for the game
    Receives click, on_enter, on_exit functions from Controller (ActionListener) 
    '''
      
    def __init__(self, params, click, on_enter_, on_exit_):
        super().__init__()
        self.board = [[0 for _ in range(8)]for _ in range(8)]
        
        self.setup_board(click, on_enter_, on_exit_)
    
    # Create and set up the buttons that are part of the game
    def setup_board(self, click, on_enter_, on_exit_):
        for r in range(8):
            for c in range(8):
                b = GameButton(self, r, c)
                b.config(bg = "green", text = "%s%s" %(r,c)
                         , command = lambda row = r, col = c: click(row, col))
                b.bind('<Enter>', lambda e, ro = r, co = c: on_enter_(ro,co)) 
                b.bind('<Leave>', lambda e, ro = r, co = c: on_exit_(ro,co)) 
                b.grid(row = r, column = c, sticky = (N,S,W,E))      
                self.board[r][c] = b
                self.columnconfigure(c, weight = 1)
            self.rowconfigure(r, weight = 1)

        self.board[3][3].configure(bg = "white")
        self.board[4][4].configure(bg = "white")
        self.board[3][4].configure(bg = "black")
        self.board[4][3].configure(bg = "black")
    
    # reset the "graphics" of the board without having to recreate the buttons    
    def reset_board(self):
        for x in range(8):
            for y in range(8):
                self.board[x][y].configure(bg = "green")
        
        self.board[3][3].configure(bg = "white")
        self.board[4][4].configure(bg = "white")
        self.board[3][4].configure(bg = "black")
        self.board[4][3].configure(bg = "black")        
        
    # move is a list of bricks to turn. [[3,3],[4,3]].
    # Change each brick to match players color
    def flip_squares(self, move, color):
        for m in move:
            self.board[m[0]][m[1]].configure(bg = color)
            
    # move is a single brick to turn. [3,4]
    def flip_single_square(self, move, color):
        self.board[move[0]][move[1]].configure(bg = color)