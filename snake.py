from turtle import Turtle, Screen
import random

color = ['purple', 'yellow', 'orange', 'pink', 'red', 'blue', 'green', 'cyan', 'brown']
screen = Screen()

class Snake:
    def __init__(self):
        self.s = []
        self.create_snake()
        self.head = self.s[-1]
        self.f = 0
        #print(f"distance btw head and 2nd head = {self.s[-1].distance(self.s[-2])}")
        #print(f"distance btw head and 3rd head = {self.s[-1].distance(self.s[-3])}")

    def create_snake(self):
        for i in range(3):
            tur = Turtle(shape="square")
            tur.penup()
            self.s.append(tur)
            tur.forward(i*20)

    def move(self):
        for i in range(len(self.s) - 1):
            p = self.s[i + 1].pos()
            self.s[i].goto(p)
        self.s[-1].forward(20)
        self.s[0].st()

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def grow_snake(self):
        ns = Turtle(shape="square")
        ns.ht()
        ns.penup()
        self.s.insert(0, ns)

    def check_collision(self):
        if 298 > self.head.xcor() > -298 and 298 > self.head.ycor() > -298:
            for i in range(len(self.s) - 2):
                if self.head.distance(self.s[i]) > 10:
                    self.f = 1
                else:
                    self.f = 0
                    break

        else:
            self.f = 0
        if self.f == 0:
            return False
        else:
            return True


class Food:
    def __init__(self):
        self.food = self.show_food()

    def show_food(self):
        food = Turtle()
        food.penup()
        food.ht()
        food.goto(random.randint(-200, 200), random.randint(-200, 200))
        food.dot(12, random.choice(color))
        return food

    def eat_food(self):
        self.food.clear()
        self.food = self.show_food()


class Score:
    def __init__(self):
        self.score = 0
        self.new_score = self.show_score()

    def show_score(self):
        s = Turtle()
        s.penup()
        s.ht()
        s.goto(x=-50, y=260)
        s.write(f"Score : {self.score}", font=('Courier', 15, 'bold'))
        return s

    def update_score(self):
        self.score += 1
        self.new_score.clear()
        self.new_score = self.show_score()

    def game_over(self):
        self.new_score.goto(0, 0)
        self.new_score.write("GAME OVER!", align='center', font=('Courier',20,'bold'))



