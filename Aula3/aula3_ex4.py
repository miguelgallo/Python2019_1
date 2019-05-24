import math

def km_to_mile(km):
    mile = km / 1.61
    print("O valor de ", "%.2f" % (km), " quilômetros corresponde a ", "%.2f" %(mile), " milhas")

def mile_to_km(mile):
    km = mile * 1.61
    print("O valor de ", "%.2f" % (mile), " milhas corresponde a ", "%.2f" %(km), " quilômetros")
    return km

def tempo_to_h(seg, minutos, h):
    h1 = seg / 3600
    h2 = minutos / 60
    h_tot = h1 + h2 + h    
    print("O valor de ", "%.2f" % (seg), "segundos e ", "%.2f" %(minutos), " minutos e ", h,"horas equivalem a ", "%.2f" % (h_tot) , " horas")
    return h_tot

def tempo_to_s(seg1):
    s1 = minutos * 60
    s2 = h * 3600
    seg1 = s1 + s2 + seg
    print("O valor de ", "%.2f" % (seg), "segundos e ", "%.2f" %(minutos), " minutos e ", h,"horas equivalem a ", "%.2f" % (seg1) , " horas")
    return h_tot_s

def velocidade_media(km,h_tot):
    vm_km = km / h_tot
    print("A velocidade média é: ", vm_km, "km/h")
    return vm_km

def tempo_km(vm_km):
    t_km = 1/vm_km
    print("O tempo gasto por km é: ", t_km, "horas")

h = float(input("Digite a quantidade de horas: "))
minutos = float(input("Digite a quantidade de minutos: "))
seg = float(input("Digite a quantidade de segundos: "))
mile = float(input("Digite o espaco em milhas: "))

km = mile_to_km(mile)

h_tot = tempo_to_h(seg,minutos,h)

vm_km = km / h_tot

velocidade_media(km,h_tot)

tempo_km(vm_km)
