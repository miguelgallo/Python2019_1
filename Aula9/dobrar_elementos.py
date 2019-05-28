class dobrar_elementos:

    def __init__(self, uma_lista, nova_lista):
        self.uma_lista = uma_lista
        self.nova_lista = nova_lista

    def dobrar_elementos(self):
        """ Escreve os elementos de uma_lista com o dobro de seus valores originais em uma nova_lista.
        """
        for (i, valor) in enumerate(self.uma_lista):
            novo_elem = 2 * valor
            self.nova_lista[i] = novo_elem

            return self.uma_lista, self.nova_lista

if __name__ == '__main__':
    minha_lista = [2, 4, 6]
    nova_lista = [0, 0, 0]
    print('Lista de input: ', minha_lista)
    print('Lista que será modificada: ', nova_lista)
    dobrar_elementos(minha_lista, nova_lista)
    print('Lista de input após rodar a função: ', minha_lista)
    print('Lista modificada após rodar a função: ', nova_lista)
    print('Verificação para ver se a lista de input é igual a lista modificada: ', minha_lista is nova_lista)

