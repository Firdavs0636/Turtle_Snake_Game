import time
from turtle import Screen
from Snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Xenzia')
screen.tracer(0, 0.1)

snake = Snake()
food = Food()
score_board = ScoreBoard()

# Makes the tKinter window listen to the keyboard click
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# Triggers the game ON
gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.10)
    snake.move()

# collision with FOOD
    if snake.head.distance(food) < 11:
        food.refresh()
        score_board.update()
        snake.extend()

# collision with WALL
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameIsOn = False
        score_board.game_over()

# collision with TAIL
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameIsOn = False
            score_board.game_over()


screen.exitonclick()
