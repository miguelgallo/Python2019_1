import turtle
bob = turtle.Turtle()

def koch(t, l):
    # t: turtle
    # l: length
    if l < 3:
        t.fd(l)
        return
    koch(t,l/3)
    t.lt(60)
    koch(t,l/3)
    t.rt(120)
    koch(t,l/3)
    t.lt(60)
    koch(t,l/3)
	
#soma dos ãngulos internos é 360 graus
def snowflake(t, l):
    koch(t, l)for i in range(3):
        koch(t, n)
        t.rt(120)

snowflake(bob, 300)

turtle.mainloop()
