'''
Created on Sep 4, 2018

@author: Eirik
'''
from logic.Ai import Ai

class Controller(object):
    '''
    Class containing the logic of the game (Reversi)
    Reacts to input from user (clicks)
    Contains a logical board, and sends commands to UI based on that
    '''
    directions = [ [-1,-1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1] ]

    # Init the board and default both AIs to 0 (human players)
    def __init__(self, params):
        #how long to wait before AI makes a move
        self.aidelay = 100
        self.empty = 2
        self.board = [[0 for _ in range(8)]for _ in range(8)]
        self.black = 0
        self.white = 1
        self.setup_board(0,0) 
        
    #setup / reset board.
    #Gets AI levels from AiSelect frame
    def setup_board(self, ai1, ai2):
        self.player = 0
        self.opponent = 1
        for row in range(8):
            for column in range(8):
                self.board[row][column] = self.empty
        self.board[3][3] = self.white
        self.board[4][4] = self.white
        self.board[3][4] = self.black
        self.board[4][3] = self.black
        self.whitecount = 2
        self.blackcount = 2
        self.emptycount = 60        
        self.ais = [Ai(ai1), Ai(ai2)]

    # x is length of move just performed. 
    # Current player gains x bricks, opponent loses x-1 and empty loses 1 
    def update_score(self, x):
        if self.player is self.black:
            self.blackcount += x
            self.whitecount -= x-1
        else: 
            self.whitecount += x
            self.blackcount -= x-1
        self.emptycount -= 1
        self.update_scoreboard(self.blackcount, self.whitecount, self.emptycount)
    
    # Display new scores
    def update_scoreboard(self, black, white, empty):
        self.game.update_score(black, white, empty)
    
    # switch player and opponent
    def change_player(self):
        self.player, self.opponent = self.opponent, self.player
        
    # Get color of current player
    def get_player_color(self):
        if self.player == self.black:
            return "black"
        return "white"
    
    # Find all legal moves and have AI select one of them
    def Ai_move(self):            
        moves = self.find_all_legal_moves()
        if moves != None and len(moves):
            move = self.ais[self.player].perform_move(moves)        
            if move != None and len(move):
                self.finish_move(move)
    
    # Update the logical board and the graphics, swap players and
    # prepare next move
    def finish_move(self, move):
        self.flip_squares(move)
        self.update_score(len(move))
        self.change_player()
        self.next_move()
            
    # Check if player has a legal move. If player doesn't have legal moves
    # ,check if opponent does. If neither has legal moves, end game. 
    # If opponent has legal moves, swap players and perform move.
    # If player can move, perform move if player is AI controlled
    # , wait for player input if not
    def next_move(self):
        if len(self.find_all_legal_moves()) == 0:
            self.update_status(self.get_player_color() + " has no legal moves, switching player")
            self.change_player()
            if len(self.find_all_legal_moves()) == 0:
                self.update_status(self.get_winner())
                return None
        
        if self.emptycount == 0:
            self.update_status(self.get_winner())
        else:
            self.update_status("Current player: %s" %self.get_player_color())
            if self.ais[self.player-1] != None:
                self.game.root.after(self.aidelay,self.Ai_move)
    
    def get_winner(self):
        if self.whitecount > self.blackcount:
            return "White wins %s - %s" %(self.whitecount, self.blackcount)
        if self.whitecount < self.blackcount:
            return "Black wins %s - %s" %(self.blackcount, self.whitecount)
        return "Game ended in a tie!"
                
    # Check if the square player clicked is a legal move.
    # If it is, flip bricks, update score and change player
    def click(self, row, column):
        move = self.check_if_legal(row, column)
        if move != None and len(move):
            self.finish_move(move)
        else:
            self.update_status("Not a legal move. Current player: %s"%self.get_player_color())
    
    def update_status(self, text):
        self.game.scoreboard.update_status(text)
            
    # Change value of the logical board and the graphical representation
    def flip_squares(self, move):
        for m in move:
            self.board[m[0]][m[1]] = self.player
        self.game.flip_squares(move, self.get_player_color())
            
    # If player hovers over a square, check if it's a legal move,
    # indicate which bricks will be turned if that move is selected.
    def on_enter_(self, row, column):
        self.temp_move = self.check_if_legal(row, column)
        if self.temp_move != None and len(self.temp_move):
            self.game.flip_squares(self.temp_move, "yellow")
     
    # Remove markers for possible move when player is no longer hovering over the square 
    def on_exit_(self, row, column):
        if self.temp_move != None and len(self.temp_move):
            for move in self.temp_move:
                self.game.game_buttons.flip_single_square(move, self.get_color(move))
        
    # Get the color according to the logical board.
    # Used to revert temporary move caused by hovering over a square 
    def get_color(self, square):
        if self.board[square[0]][square[1]] == self.black:
            return "black"
        if self.board[square[0]][square[1]] == self.white:
            return "white"
        if self.board[square[0]][square[1]] == self.empty:
            return "green"
        
    # Scan entire board to determine all legal moves so that AI has a list to consider
    def find_all_legal_moves(self):
        legal_moves = []
        for row in range(8):
            for column in range(8):
                move = self.check_if_legal(row, column)
                if move != None and len(move):
                    legal_moves.append(move)
        return legal_moves
    
    # Check every direction if this move would turn any bricks. 
    # if anything will be turned also add current square to the move 
    def check_if_legal(self, row, column):
        if self.board[row][column] != self.empty:
            return None
        move = []
        for direction in self.directions:
            movedir = self.check_direction(row, column, direction)
            if movedir != None:
                move.extend(movedir)
        if move != None and len(move):
            move.append([row, column])
        return move
    
    # Check for legal move in one direction. If neighbor is outside board,
    # empty or same brick as current player return None (not a valid direction)
    # If neighbor is opponent, continue till next brick in direction isn't opponent.
    # if direction encounters current player(legal move), return the move.         
    def check_direction(self, row, column, direction):
        move= []
        if 0 > row + direction[0] or row + direction[0] > 7 or 0 > column + direction[1] or column + direction[1] > 7:
            return None
        if self.board[row + direction[0]][column + direction[1]] != self.opponent:
            return None
        move.append([row + direction[0], column + direction[1]])
        for x in range(2, 8):
            if row + direction[0] * x > 7 or row + direction[0] * x < 0 or column + direction[1] * x < 0 or column + direction[1] * x > 7:
                return None
            if self.board[row + direction[0] * x][column + direction[1] * x] == self.opponent:
                move.append([row + direction[0] * x, column + direction[1] * x])
            if self.board[row + direction[0] * x][column + direction[1] * x] == self.player:
                return move
            if self.board[row + direction[0] * x][column + direction[1] * x] == self.empty:
                return None
    
    # Reset logical board and UI. Create AIs. If player1 is AI, make move.        
    def start_game(self, player1, player2):
        self.setup_board(player1, player2)
        self.game.reset_board()
        self.update_scoreboard(2, 2, 60)
        if self.ais[self.player].level != 0:
            self.game.root.after(self.aidelay,self.Ai_move)