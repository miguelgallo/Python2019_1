import turtle

jn = turtle.Screen()                 # Configurar a janela e seus atributos
jn.bgcolor("lightblue")              # Selecionar cor de fundo
jn.title("Teca & Joana")             # Definir título

bob = turtle.Turtle()                  # Criar Bob
bob.shape("turtle")                    # Selecionar formato         
bob.color("black")                     # Selecionar cor
bob.pensize(5)                         # Selecionar largura       
bob.speed("normal")                    # Selecionar velocidade

print("Choose the lenght : ")  
lenght = eval(input('Lenght: '))
print("Choose the number of angles : ")  
n_poly = eval(input('Number of angles: '))
angle = 360/int(n_poly) 

def square(t, l):
    for i in range(4):
        t.forward(l)               
        t.left(90)

def polygon(t, l, a):
    for i in range(int(n_poly)):
        t.forward(l)                
        t.left(a)
        
polygon(bob, lenght, angle)
