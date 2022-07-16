"""
Project No. Red Alert
Two stars appear and start moving down the screen. The player needs to click on the red star before the stars
reach the bottom of screen. For each level, more stars are added. if you click on a non-red star, you lose

project on the animate() function in pygame zero
update() function

Hacks and Tweaks
change the star icon to something else

make the stars move at different speeds

make the stars shuffle every couple of seconds --> create a function

try again
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

def draw(): #add some stars to the screen and display message the draw() function is cllaed when an update() function has been defined, the clock event fires, or an input has been triggered
    global stars, current_level, game_over, game_complete
    screen.clear()
    screen.blit("space",(0,0))
    if game_over: #if game_over is true
        display_message("GAME OVER!", "Try Again.")
    elif game_complete:
        display_message("YOU WON","Well Done.")
    else: #if the game isn't over, then draw stars on the screen from the list of stars
        for star in stars:
            star.draw()

def update():
    global stars
    if len(stars) == 0: #if there are no stars in the list, that means we are at the beginnning of the game or at the end of the level when a red star is clicked
        stars = create_level(current_level) #re-populate the list of stars


#in order to make new stars, you must create a list of colors,  a least of actor "star" objects, layout the stars in order on the top of the screen, and animate the new stars list
def create_level(stars_num): #depending on the level, a number of stars are added.
    colors_to_create = get_colors_to_create(stars_num) # a list of colors ["red","blue",etc]
    new_stars = create_stars(colors_to_create) #input is a list of colors
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars


def get_colors_to_create(num):
    colors_to_create = ["red"] #first item in the list will always be red
    for i in range(num): #iterate through a length of the number of extra stars being added
        random_color = random.choice(COLORS) #choose a random item from the COLORS list
        colors_to_create.append(random_color) #add it to the list
    return colors_to_create #return the list of colors

def create_stars(color_list):
    new_stars = [] #create an empty list of new stars
    for color in color_list:
        star = Actor(color + "-star")
        new_stars.append(star)
    return new_stars

def layout_stars(star_list):
    gap_num = len(star_list) + 1 #calculate the number of gaps on the screen
    gap_size = WIDTH / gap_num
    random.shuffle(star_list)
    # for index, star in enumerate(star_list): #enumerate will return a list of tuples like so .. [(0,star1),(1,star2),(2,star3)...]
    #     x_pos = (index+1) * gap_size # xctrl+/ to block comment
    #     star.x = x_pos #change the x position of the new star
    #or
    for index in range(len(star_list)):
        x_pos = (index+1) * gap_size
        star_list[index].x = x_pos

def animate_stars(star_list):
    for star in star_list:
        duration = random.randint(current_level+1,START_SPEED)-current_level
        #duration = (START_SPEED-random.randint(1,9)) - current_level #the higher the level, the shorter the duration of the level
        print('the duration for {} is {}'.format(star.image,duration))
        star.anchor = ("center", "bottom") #sets the anchor of the star at the bottom of the star image
        animation = animate(star, duration=duration, on_finished=handle_game_over,x=random.randint(10,WIDTH-10),y=HEIGHT)
        #print(type(animation))
        #animate(on_finished = call a function when animation finishes, y=move actor down a number of pixels
        animations.append(animation) #hold the animations in a list of animation objects


def shuffle():
    global stars
    if stars:
        x_values = [star.x for star in stars] #loops through the x values of each star in puts in x_values list
        random.shuffle(x_values)
        for indexb;''
def on_mouse_down(pos):
    global stars, current_level
    for star in stars:
        if star.collidepoint(pos):
            if "red" in star.image:
                red_star_click()
            else: #didn't click on the red star so game is over
                handle_game_over()

def red_star_click():
    global current_level, stars, animations, game_complete
    stop_animations(animations) #if the user clicks the red star. all of the animations must stop
    if current_level == FINAL_LEVEL:
        game_complete = True
    else: #user reached next level, set animations and star lists to empty and increase level number
        current_level += 1
        stars = [] #an empty star list will trigger the create_level() in the update function
        animations = []

def stop_animations(animation_list):
    for animation in animation_list:
        if animation.running:
            animation.stop()

def handle_game_over():
    global game_over
    game_over = True

def display_message(message1,message2):
    screen.draw.text(message1,fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(message2, fontsize=30, center=(CENTER_X, CENTER_Y+30), color=FONT_COLOR)



pgzrun.go()