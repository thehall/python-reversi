'''
Created on Sep 4, 2018

@author: Eirik
'''
import random
class Ai(object):
    '''
        "AI" class that receives a list of possible moves, and selects one of them
        based on difficulty setting 
    '''
    # Set difficulty level of AI.
    # (0 = None(player), 1 = random moves, 2 = greedy moves, 3 = valued moves)
    def __init__(self, level):
        self.level = level
            
    def perform_move(self, moves):
        if self.level == 1:
            return self.perform_move_random(moves)
        if self.level == 2:
            return self.perform_move_greedy(moves)
        if self.level == 3:
            return self.perform_move_value(moves)
        
    # Simplest AI, simply select a random move from the list of possible moves
    def perform_move_random(self, moves):
        select = random.randrange(len(moves))
        return moves[select]
    
    # Select the move that results in most bricks being turned
    # (if two or more moves is the greediest move, return one of them at random)
    def perform_move_greedy(self, moves):
        longest = 0
        longest_move = []
        for move in moves:
            if len(move) == longest:
                longest_move.append(move)
            if len(move) > longest:
                longest = len(move)
                longest_move = []
                longest_move.append(move)
        return longest_move[random.randrange(len(longest_move))]
    
    # Values indicating how "good" a square is to have.
    square_values = [ 
            [99, -8, 8,  6,  6,  8,  -8, 99], 
            [-8, -24,  -4, -3, -3, -4, -24,  -8],  
            [8, -4, 7,  4,  4,  7,  -4, 8], 
            [6,  -3, 4,  0,  0,  4,  -3, 6],  
            [6,  -3, 4,  0,  0,  4,  -3, 6],
            [8,  -4, 7,  4,  4,  7,  -4, 8],
            [-8, -24,  -4, -3, -3, -4, -24, -8],
            [99, -8, 8,  6,  6,  8,  -8, 99] 
          ]
    
    # Check final square of each move (where new brick would be placed) and find
    # value of that square. Select the move where the new brick has the highest value.
    # If two or more moves have equal value, return a random one of them.
    def perform_move_value(self, moves):
        best = -99
        best_move = []
        for move in moves:
            last_pos = move[-1]
            if self.square_values[ last_pos[0] ][ last_pos[1] ] == best:
                best_move.append(move)
            if self.square_values[ last_pos[0] ][ last_pos[1] ] > best:
                best = self.square_values[ last_pos[0] ][ last_pos[1] ]
                best_move = []
                best_move.append(move)
        return best_move[random.randrange(len(best_move))]
             