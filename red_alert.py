"""
Project No. Red Alert
Two stars appear and start moving down the screen. The player needs to click on the red star before the stars
reach the bottom of screen. For each level, more stars are added. if you click on a non-red star, you lose

project on the animate() function
update() function
"""
import random, pgzrun


#DECLARE CONSTANTS -> constants are vars declared at the start of the program. Their vals shouldn't change throughout the program
FONT_COLOR = (255,255,255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH /2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X,CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
COLORS = ["green","blue"]

#DECLARE GLOBAL VARIABLES
game_over = False
game_complete = False
current_level = 1
stars = []
animations = []

def draw(): #add some stars to the screen and display message
    global stars, current_level, game_over, game_complete
    screen.clear()
    screen.blit("space",(0,0))
