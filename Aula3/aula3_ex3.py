import math

def ang_zenital(altura, sombra):
    tan = sombra / altura
    ang_rad = (math.atan(tan))
    ang_graus = (math.degrees(ang_rad)) 
    print("O ângulo é aproximadamente: ", "%.2f" % (ang_rad) , " radianos e corresponde a ", "%.2f" %(ang_graus), " graus.")

sombra = float(input("Digite o tamanho da sombra: "))

altura = float(input("Digite a altura do objeto: "))

ang_zenital(altura, sombra)
