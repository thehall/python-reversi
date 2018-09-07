'''
Created on Sep 4, 2018

@author: Eirik
'''
from ui.GameFrame import GameFrame
from logic.Controller import Controller
if __name__ == '__main__':
    controller = Controller("Name")
    # Pass click, on_enter, on_exit, and start_game from Controller to UI section (actionlistener)  
    gameframe = GameFrame("Name", controller.click, controller.on_enter_, controller.on_exit_, controller.start_game)
    # Give the controller access to the UI section
    controller.game = gameframe
    controller.game.start()
   
    pass