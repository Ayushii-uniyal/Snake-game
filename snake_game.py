import turtle as t
import snake
import time

s = t.Screen()
s.setup(600, 600)
s.tracer(0)

snakes = snake.Snake()
foods = snake.Food()

s.listen()
s.onkey(snakes.up, "Up")
s.onkey(snakes.down, "Down")
s.onkey(snakes.right, "Right")
s.onkey(snakes.left, "Left")

score = snake.Score()
condition = snakes.check_collision()
while condition:
    s.update()
    time.sleep(.1)
    snakes.move()
    if snakes.head.distance(foods.food) < 15:
        foods.eat_food()
        snakes.grow_snake()
        score.update_score()
    condition = snakes.check_collision()
score.game_over()