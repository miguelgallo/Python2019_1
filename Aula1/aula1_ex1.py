print('Programa usado para converter quilômetros em milhas, calcula o tempo médio gasto por milha e a velocidade média em milhas por horas')

d = input('Insira a distância em quilômetro: ')

milha = float(d)/1.61

print('A distância ', d, ' quilômetros representa ', milha, 'milha')
print('Agora separe o tempo em 3 partes: horas, minutos e segundos')

h= input('Insira a quantidade de horas: ')

min = input('Insira a quantidade de minutos: ')
min = float(min) / 60

s = input('Insira a quantidade de segundos: ')
s = float(s)/3600

h_tot =  float(h) + min + s

print('A quantidade de horas: ', h_tot)

vm = milha/h_tot

print('A velocidade média é: ', vm, 'milhas/horas')

tempo = 1 / vm

print('O tempo gasto para percorrer uma milha:', tempo, 'horas')
