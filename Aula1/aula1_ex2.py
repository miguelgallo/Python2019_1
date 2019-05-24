print('Programa usado para calcular a distância entre o expectador de uma queima de fogos de atifícios do Reveillon')

v_som = 343 #em m/s

print('Supondo que a luz chega aos olhos do observador depois de um tempo muito pequeno, ou seja, o tempo de chegada da luz até o observador é aproximadamente zero. Considerando a velocidade do som igual a: ',  v_som,'m/s.') 

t_som = input('Insira o tempo que o som demorou para chegar: ')

distancia = (float(t_som))*(int(v_som))

print('A distância entre o local da queima de fogos e o observador é de: ', "%.2f" % distancia, 'metros')
