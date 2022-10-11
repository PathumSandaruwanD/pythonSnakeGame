from tkinter import *
import random

GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 50
SPACE_SIZE = 50
SNAKE_PARTS = 3
SNAKE_COLOR = "yellow"
FOOD_COLOR ="red"
BACKGROND_COLOR = "black"



class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collision():
    pass

def game_over():
    pass

window = Tk();
window.title("Snake Game")
window.resizable(False, False)

score = 0;
direction = 'down'
lable = Label(window, text="Score:{}".format(score), font=('consolas',40))
lable.pack()

canvas = Canvas(window, bg=BACKGROND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.mainloop()