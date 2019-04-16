import turtle

binning = eval(input('Coloque o bin desejado: '))

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(binning)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()             # Added this line

wn = turtle.Screen()         # Set up the window and its attributes
print("Choose the background color : ")  
wn.bgcolor(input('Background Color: '))

tess = turtle.Turtle()       # Create tess and set some attributes
print("Choose the turtle line and fill color : ")  
tess.color(input('Line Color: '), input('Fill Color: '))
tess.pensize(3)

tess.pu()
tess.bk(150)
tess.rt(90)
tess.fd(100)
tess.lt(90)
tess.pd()

xs = [int(x) for x in input().split()]
#xs = eval(input(' '))

try:
    xs = xs + [] #duck typing
    print("O argumento é uma lista")

except TypeError:
    print("O argumento não é uma lista")

for a in xs:
    draw_bar(tess, a)

wn.mainloop()
