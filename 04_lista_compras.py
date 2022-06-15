
"""Fazer uma lista de compras e apresentar na tela"""



carrinho = []
produto = ''

while produto != 'sair':
    print("Insira um produto no carrinho ou digite 'sair' para encerrar.")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

