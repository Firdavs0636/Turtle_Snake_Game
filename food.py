from turtle import Turtle
import random

# Creating food class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.speed('fastest')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('#55f4ec')
        self.refresh()

# Puts food to random places on the screen
    def refresh(self):
        random_x = random.randint(a=-280, b=280)
        random_y = random.randint(a=-280, b=280)
        self.goto(x=random_x, y=random_y)

