'''Pygame implementation of TicTacToe Game - A starter project to demonstrate the use of Classes and Objects in Python.
This was designed completely using pygame
Code inspired from Geeks for Geeks Tutorial
source link : https://www.geeksforgeeks.org/tic-tac-toe-gui-in-python-using-pygame/
 '''

#Pygame imports
import pygame as pg
from pygame.locals import *
# initializing the pygame window 
pg.init()
pg.display.set_caption("Tic Tac Toe game")

#Other imports
import sys,time


class TicTacToe:
    def __init__(self):
        #Initial values
        self.XO = 'x' 
        self.winner = None
        self.draw = None
        self.width = 400
        self.height = 400
        #Background of game window
        self.white = (255, 255, 255) 
        self.line_color = (0,0,0)
        self.board = [[None]*3, [None]*3, [None]*3] 
        self.fps = 30
        self.CLOCK = pg.time.Clock() 
        self.screen = pg.display.set_mode((self.width, self.height + 100), 0, 32)  
        self.initiating_window = pg.image.load("./assets/modified_cover.png") 
        self.x_img = pg.image.load("./assets/X_modified.png") 
        self.y_img = pg.image.load("./assets/o_modified.png") 
        self.initiating_window = pg.transform.scale(self.initiating_window, (self.width, self.height + 100)) 
        self.x_img = pg.transform.scale(self.x_img, (80, 80)) 
        self.o_img = pg.transform.scale(self.y_img, (80, 80))

    def draw_status(self): 
        if self.winner is None: 
            self.message = self.XO.upper() + "'s Turn"
        else: 
            self.message = self.winner.upper() + " won !"
        if self.draw: 
            self.message = "Game Draw !"
        self.font = pg.font.Font(None, 30) 
        self.text = self.font.render(self.message, 1, (255, 255, 255)) 
        self.screen.fill ((0, 0, 0), (0, 400, 500, 100)) 
        self.text_rect = self.text.get_rect(center =(self.width / 2, 500-50)) 
        self.screen.blit(self.text, self.text_rect) 
        pg.display.update()     

    def game_initiating_window(self):  
        self.screen.blit(self.initiating_window, (0, 0)) 
        pg.display.update() 
        time.sleep(3)					 
        self.screen.fill(self.white)  
        pg.draw.line(self.screen, self.line_color, (self.width / 3, 0), (self.width / 3, self.height), 7) 
        pg.draw.line(self.screen, self.line_color, (self.width / 3 * 2, 0), (self.width / 3 * 2, self.height), 7) 
        pg.draw.line(self.screen, self.line_color, (0, self.height / 3), (self.width, self.height / 3), 7) 
        pg.draw.line(self.screen, self.line_color, (0, self.height / 3 * 2), (self.width, self.height / 3 * 2), 7) 
        self.draw_status() 

    def check_win(self): 
        # global board, winner, draw 
        for row in range(0, 3): 
            if((self.board[row][0] == self.board[row][1] == self.board[row][2]) and (self.board [row][0] is not None)): 
                self.winner = self.board[row][0] 
                pg.draw.line(self.screen, (250, 0, 0),(0, (row + 1)*self.height / 3 -self.height / 6), (self.width, (row + 1)*self.height / 3 - self.height / 6 ),4) 
                break
        for col in range(0, 3): 
            if((self.board[0][col] == self.board[1][col] == self.board[2][col]) and (self.board[0][col] is not None)): 
                self.winner = self.board[0][col] 
                pg.draw.line (self.screen, (250, 0, 0), ((col + 1)* self.width / 3 - self.width / 6, 0),((col + 1)* self.width / 3 - self.width / 6, self.height), 4) 
                break
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and (self.board[0][0] is not None): 
            self.winner = self.board[0][0] 
            pg.draw.line (self.screen, (250, 70, 70), (50, 50), (350, 350), 4)      
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and (self.board[0][2] is not None): 
            self.winner = self.board[0][2] 
            pg.draw.line (self.screen, (250, 70, 70), (350, 50), (50, 350), 4) 
        if(all([all(row) for row in self.board]) and self.winner is None ): 
            self.draw = True
        self.draw_status()    
    
    def drawXO(self,row,col): 
        if row == 1: 
            self.posx = 30	 
        if row == 2: 
            self.posx = self.width / 3 + 30    
        if row == 3: 
            self.posx = self.width / 3 * 2 + 30
        if col == 1: 
            self.posy = 30     
        if col == 2: 
            self.posy = self.height / 3 + 30  
        if col == 3: 
            self.posy = self.height / 3 * 2 + 30 
        self.board[row-1][col-1] = self.XO 
        
        if(self.XO == 'x'): 
            self.screen.blit(self.x_img, (self.posy, self.posx)) 
            self.XO = 'o' 
        else: 
            self.screen.blit(self.o_img, (self.posy, self.posx)) 
            self.XO = 'x'    
        pg.display.update() 

    def user_click(self): 
        x, y = pg.mouse.get_pos() 
        if(x<self.width / 3): 
            col = 1
        elif (x<self.width / 3 * 2): 
            col = 2
        elif(x<self.width): 
            col = 3
        else: 
            col = None
        if(y<self.height / 3): 
            row = 1
        
        elif (y<self.height / 3 * 2): 
            row = 2
        
        elif(y<self.height): 
            row = 3       
        else: 
            row = None
        if(row and col and self.board[row-1][col-1] is None): 
            self.drawXO(row, col) 
            self.check_win()     
    def reset_game(self): 
        time.sleep(3) 
        self.XO = 'x'
        self.draw = False
        self.game_initiating_window() 
        self.winner = None
        self.board = [[None]*3, [None]*3, [None]*3]

    def initialise_game(self):
        self.game_initiating_window() 
        while(True): 
            for event in pg.event.get(): 
                if event.type == QUIT: 
                    pg.quit() 
                    sys.exit() 
                elif event.type is MOUSEBUTTONDOWN: 
                    self.user_click() 
                    if(self.winner or self.draw): 
                        self.reset_game() 
            pg.display.update() 
            self.CLOCK.tick(self.fps) 

game = TicTacToe()
game.initialise_game()
