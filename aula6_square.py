import turtle

jn = turtle.Screen()                 # Configurar a janela e seus atributos
jn.bgcolor("lightblue")              # Selecionar cor de fundo
jn.title("Teca & Joana")             # Definir título

bob = turtle.Turtle()                  # Criar Bob
bob.shape("turtle")                    # Selecionar formato         
bob.color("black")                     # Selecionar cor
bob.pensize(5)                         # Selecionar largura       
bob.speed("fastest")                    # Selecionar velocidade

print("Choose the lenght : ")  
lenght = eval(input('Lenght: '))
print("Choose the number of angles : ")  
n_poly = eval(input('Number of angles: '))
print("Choose the radius : ")  
radius = eval(input('Radius: '))

def square(t, l):
    for i in range(4):
        t.forward(l)               
        t.left(90)

def polygon(t, l, n_poly):
    angle = 360/int(n_poly)
    for i in range(int(n_poly)):
        t.forward(l)                
        t.left(angle)

def circle(t, r):
     c = 2 * 3.1415 * r
     l = c / 360
     polygon(t, l, 360)
        
circle(bob, radius)
