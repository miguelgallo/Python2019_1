import turtle
jn = turtle.Screen()                     # Configurar a janela e seus atributos
print("Choose the background color : ")  
jn.bgcolor(input('Color: '))             # Selecionar cor de fundo
jn.title("Teca & Joana")                 # Definir título

joana = turtle.Turtle()                  #Criar Joana
joana.shape("turtle")                    # Selecionar formato de Joana
print("Choose Joana's color: ")          
joana.color(input('Color: '))            # Selecionar cor de Joana
print("Choose Joana's pensize: ")
joana.pensize(eval(input('Pensize: ')))  # Selecionar largura de Joana
print("Choose Joana's speed: ")          
joana.speed(input('Speed: '))            # Selecionar velocidade de Joana


for i in range(4):
    for i in range(5):                       # Loop que faz o quadrado
        joana.forward(100)
        joana.right(144)

    joana.penup()
    joana.left(90)
    joana.forward(200)                      # Comandos para mover Joana 
    joana.pendown()

