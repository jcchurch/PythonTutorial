import turtle

def makeTurtle(color1, color2):
    t = turtle.Turtle()
    t.shape('turtle')
    t.color(color1, color2)
    return t

window = turtle.Screen()
t = makeTurtle('green', 'yellow')

numberOfCircles = int(input('How many circles should I draw?    '))

for i in range(numberOfCircles):
    t.circle(100)
    t.left(360 / numberOfCircles)

window.mainloop()
