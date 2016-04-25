import turtle
john = turtle.Turtle()
john.speed("fastest")
john.hideturtle()
john.pensize(2)

def polygon(side,ngon,colour="black",skip=1):
  john.color(colour)
  for i in range(ngon):
    john.forward(side)
    john.right((360.0/ngon)*skip)

def polycircle(side,num,ngon,colour="black"):
  for i in range(num):
    polygon(side,ngon,colour)
    john.right(360.0/num)

def polycircles(side,num,ngon,bigRadius,numCircles,colours=["black"]):
  for i in range(numCircles):
    col=colours[i%len(colours)]
    john.up()
    john.forward(bigRadius)
    john.down()
    polycircle(side,num,ngon,col)
    john.up()
    john.backward(bigRadius)
    john.right(float(360)/numCircles)
    john.down()

for i in range(1,10):
  polycircle(side=10*(1+i),num=10,ngon=i+2,colour="black")

polycircles(side=50,num=10,ngon=5,bigRadius=300,numCircles=10,colours=["blue","red"])

