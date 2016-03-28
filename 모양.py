import turtle

wn=turtle.Screen()

t1=turtle.Turtle()

width=t1.window_width()

w3=(width-23)/3

x1=0-w3

pos1=((x1,0))

pos2=((x1+200,0))

pos3=((x1+500,0))

def drawTriangle(size,pos1):
    t1.penup()
    t1.setpos(pos1)
    t1.pendown()
    t1.fd(size)
    t1.left(120)
    t1.fd(size)
    t1.left(120)
    t1.fd(size)
    

size=100

def drawPolygon(size,pos2):
   t1.penup()
   t1.setpos(pos2)
   t1.pendown()
   t1.fd(size)
   t1.left(60)
   t1.fd(size)
   t1.left(60)
   t1.fd(size)
   t1.left(60)
   t1.fd(size)
   t1.left(60)
   t1.fd(size)
   t1.left(60)
   t1.fd(size)
   

def drawStar(size,pos3):
  t1.penup()
  t1.setpos(pos3)
  t1.pendown()
  t1.fd(size)
  t1.right(144)
  t1.fd(size)
  t1.right(144)
  t1.fd(size)
  t1.right(144)
  t1.fd(size)
  t1.right(144)
  t1.fd(size)
  

drawTriangle(size,pos1)

drawPolygon(size,pos2)

drawStar(size,pos3)

wn.exitonclick()