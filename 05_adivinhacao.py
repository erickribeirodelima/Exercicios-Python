
# Criar um programa que tenha um número secreto e a pessoa tem que digitar para descobrir.

# Importanto bibliotecas

import random
import os

os.system("cls") # limpar terminal

numero_secreto = random.randint(0,10)
numero_digitado = 0
tentativas = [] # Minha lista
total_tentativas = 5

# while numero_secreto != numero_digitado:
for x in range(total_tentativas):
    numero_digitado = int(input("Digite um número entre 0 e 20: "))
    tentativas.append(numero_digitado)
    print(tentativas)

    if numero_digitado == numero_secreto:
        print("Isso mesmo, você acertou! o numero secreto era: " + str(numero_digitado))
        break
    else:
        print("Não é esse número, rs.")
        if numero_digitado > numero_secreto:
            print("O número que você digitou é MAIOR...")
            
        if numero_digitado < numero_secreto:
            print("O número que você digitou é MENOR...")
    

print("Jogo finalizado! Até a próxima ;)")

