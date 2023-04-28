import turtle as t
import random


def reset():
  t.reset()


def setup():
  t.speed(0)
  t.screensize(1000, 1000)
  t.pensize(2)


def drawRectangle(height, width):
  t.fd(height)
  t.right(90)
  t.fd(width)
  t.right(90)
  t.fd(height)
  t.right(90)
  t.fd(width)
  t.right(90)


def setRandomColor():
  return random.choice(["purple", "blue", "dark green", "black"])


def drawRectanglePattern(x, y, offset, width, height, count, rotation):
  circ = offset * 2 * 3.14
  angle = 360 / count
  inc = circ / count
  
  t.penup()
  t.goto(x + offset, y)
  t.seth(90)
  t.right(45)
  t.pendown()
  for i in range(count):
    t.color(setRandomColor())
    drawRectangle(height, width)
    t.penup()
    t.left(rotation + angle)
    t.fd(inc)
    t.right(rotation)
    t.pendown()


def drawCirclePattern(x, y, offset, radius, count):
  angle = 360/count
  circ = 2 * 3.14 * offset
  inc = circ/count
  
  t.penup()
  t.goto(x + offset, y)
  t.seth(90)
  for i in range(count):
    t.color(setRandomColor())
    t.pendown()
    t.right(90)
    t.circle(radius)
    t.left(90)
    t.penup()
    t.left(angle)
    t.fd(inc)


def drawSuperPattern():
    t.speed(0)
    y = random.randint(-50, 50)
    offset = random.randint(-100, 100)
    x = random.randint(-50, 50)
    count = random.randint(25, 250)
    angle = random.randint(-179, 179)
    inc = 360 / count
    t.penup()
    t.goto(x + offset, y)
    t.seth(90)
    for i in range(count):
        choice = random.choice(["rect", "cir"])
        if choice == "rect":
            t.color(setRandomColor())
            height = random.randint(20, 200)
            width = random.randint(20, 200)
            t.right(angle)
            t.pendown()
            drawRectangle(height, width)
            t.penup()
            t.left(angle + inc)
            t.fd(inc)
        else:
            t.color(setRandomColor())
            t.right(angle)
            t.pendown()
            t.circle(random.randint(20, 100))
            t.penup()
            t.left(angle + inc)
            t.fd(inc)


def done():
  t.done()
