'''
Created on Sep 4, 2018

@author: Eirik
'''
from tkinter import Button
class GameButton(Button):
    '''
    Currently a regular tkinter.Button with ability to store row/column
    TODO: add graphics / animation
    '''
    def __init__(self, master, row, column):
        Button.__init__(self, master)
        self.row = row
        self.column = column