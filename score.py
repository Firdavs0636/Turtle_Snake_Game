from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.ht()
        self.goto(x=0, y=275)
        self.scores = 0
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f'Score: {self.scores}', align=ALIGNMENT, font=FONT)
        self.scores += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)




