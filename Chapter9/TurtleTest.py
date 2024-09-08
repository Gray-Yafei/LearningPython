import turtle, time

from MyPackage import MyTools

pen = turtle.Turtle()
pen.backward(200)
pen.speed(0)
while True:
    time.sleep(1)
    pen.clear()
    times = MyTools.getTime()
    pen.write(times, font=('Arial', 40,'normal'))

