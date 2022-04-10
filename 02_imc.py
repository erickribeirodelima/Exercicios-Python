"""

02 - Digite um programa que pergunte seu nome, sua idade, seu peso, sua altura e nos mostre seu imc se está abaixo do peso,
peso adequado ou acima do peso.

"""

nome = input("Olá, digite seu nome por gentileza: ").strip().title()
idade = int(input(f"Olá {nome}, qual a sua idade? "))
peso = float(input(f"{nome}, agora digite seu peso por gentileza: "))
altura = float(input(f"Agora para finalizar, digite sua altura: "))
imc = peso / (altura * altura)


print(f"Olá {nome}, você tem {idade} anos de idade.")
print(f"E a partir dos dados sobre seu peso e altura, seu IMC é {imc:.1f}")

if imc <= 18.5:
    print("A classificação do seu IMC é 'Abaixo do Peso'.")
elif imc > 18.5 and imc <= 24.9:
    print("A classificação do seu IMC é 'Peso Normal'.")
elif imc >= 25 and imc <= 29.9:
    print("A classificação do seu IMC é 'Sobrepeso'.")
elif imc >= 30 and imc <= 34.9:
    print("A classificação do seu IMC é 'Obesidade Grau I'.")
elif imc >= 35 and imc <= 39.9:
    print("A classificação do seu IMC é 'Obesidade Grau II'.")
elif imc >= 40:
    print("A classificação do seu IMC é 'Obesidade Grau III ou Mórbida'.")
else:
    print("Valor inválido")



