import turtle
john = turtle.Turtle()
john.speed("fastest")

def square(side):
  for i in range(4):
    john.forward(side)
    john.right(90)

def squircle(side,num):
  for i in range(num):
    square(side)
    john.right(360.0/num)

def squircles(side,num,bigRadius,numSquircles):
  for i in range(numSquircles):
    john.up()
    john.forward(bigRadius)
    john.down()
    squircle(side,num)
    john.up()
    john.backward(bigRadius)
    john.right(float(360)/numSquircles)

squircles(side=75,num=17,bigRadius=275,numSquircles=5)
