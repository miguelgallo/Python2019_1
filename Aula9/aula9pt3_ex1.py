from dobrar_elementos import*

minha_lista = [2, 4, 6]
nova_lista = [0, 0, 0]

print('Lista de input: ', minha_lista)
print('Lista que será modificada: ', nova_lista)
dobrar_elementos(minha_lista, nova_lista)
print('Lista de input após rodar a função: ', minha_lista)
print('Lista modificada após rodar a função: ', nova_lista)
print('Verificação para ver se a lista de input é igual a lista modificada: ', minha_lista is nova_lista)
