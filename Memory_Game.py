#Seong Ma

import random, pygame, sys
from pygame.locals import *

#CONSTANTS FOR GAME
FPS = 60 # program framerate
WINDOW_WIDTH = 640 #game window width
WINDOW_HEIGHT = 480 #game window height
REVEAL_SPEED = 8 #the speed in which boxes will be revealed
BOX_SIZE = 40 # size of box height & width in pixels
BOX_SPACE = 10 # the space between boxes

#COLOR CONSTANTS
GRAY      = (100, 100, 100)
NAVY_BLUE = ( 60,  60, 100)
WHITE     = (255, 255, 255)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
BLUE      = (  0,   0, 255)
YELLOW    = (255, 255,   0)
ORANGE    = (255, 128,   0)
PURPLE    = (255,   0, 255)
CYAN      = (  0, 255, 255)
COLORS    = {GRAY, NAVY_BLUE, WHITE, RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN}

#SHAPE CONSTANTS
RING    = "ring"
SQUARE  = "square"
DIAMOND = "diamond"
X_SHAPE = "x_shape"
CIRCLE  = "circle"
SHAPES  = {RING, SQUARE, DIAMOND, X_SHAPE, CIRCLE}


class Memory_Game:
    def __init__(self):
        self.group_size = 8
        self.main_board = None
        self.revealed = None
        self.board_height = 0
        self.board_width = 0
        self.mouse_x = 0
        self.mouse_y = 0
        pass
    
    def Choose_Difficulty(self, pygame_initialized):
        '''
        used to select the difficulty, this will in turn
        be used to select the number of boxes used for the
        memory game, will decide the board_height and board_width
        '''
        pass
    
    def Play_Game(self):
        
        #initialize pygame
        pygame.init()
        DISPLAY_SURFACE = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Memory Block Game")
        
        #self.Choose_Difficulty()
        
        self.get_random_board()
        self.revealed = self.get_revealed(False)
        
        self.start_animation()
        
    
    def get_random_board(self):
        temp_images = []
        for color in COLORS:
            for shape in SHAPES:
                temp_images.append((shape,color))
        
        random.shuffle(temp_images)
        
        number_of_icons_used = int(self.board_height * self.board_width) / 2
        temp_images = temp_images[:number_of_icons_used]
        
        self.main_board = []
        for x in range(self.board_width):
            temp_col = []
            for y in range(self.board_height):
                temp_col.append(temp_images[0])
                temp_images = temp_images[1:]
            self.main_board.append(temp_col)
        
    def get_revealed(self, revealed_value: bool):
        temp = []
        for i in range(self.board_width):
            temp.append([revealed_value] * self.board_height)
        return temp
    
    def start_animation(self):
        #this function will reveal the boxes at the
        #beginning of the game for a short time
        temp_covered_boxes = self.get_revealed()
        temp_boxes = []
        for x in range(self.board_width):
            for y in range(self.board_height):
                temp_boxes.append((x,y))
        random.shuffle(temp_boxes)
        temp_box_groups = self.split_board_into_groups(8, temp_boxes)
    
    def split_board_into_groups(self, group_size, containers):
        temp = []
        for i in range(0, len(containers), group_size):
            temp.append(containers[i: i + group_size])
        return temp
            
        
        