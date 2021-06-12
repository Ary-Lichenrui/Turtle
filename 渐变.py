import turtle as tt
import random
  
    
def star():
    randomX=random.randint(-400,400)
    randomY=random.randint(-300,300)
    Starsize=random.randint(5,25)
    tt.up()
    tt.goto(randomX,randomY)
    tt.down()
    tt.begin_fill()
    for i in range(5):
        tt.fd(Starsize)
        tt.right(144)
    tt.end_fill()
tt.setup(800,600)
tt.speed(0)
tt.pensize(5)
tt.colormode(255)
for i in range(120):
    tt.goto(-400,300-(i*5))
    tt.pencolor(((i*2),0,255-(i*2)))
    tt.fd(800)
tt.up()
tt.goto(230,-200)
tt.pencolor('palegreen')
tt.write("星空",font=('楷体',50))
tt.pencolor('snow')
tt.pensize(1)
tt.fillcolor('yellow')
for i in range(15):
    tt.right(random.randint(0,90))
    star()
    
