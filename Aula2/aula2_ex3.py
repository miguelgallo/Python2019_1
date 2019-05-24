print ('Calculando o custo total de livros')

preco = 24.95

print(preco)

desconto = 40/100

print(desconto)

quantidade = 60

print(quantidade)

envio = 3.0 + (quantidade - 1)*0.75

preco_total = (preco * (1 - desconto) * quantidade) + envio

print('O valor total pago deve ser de: ', "%.2f" % preco_total, 'reais')
