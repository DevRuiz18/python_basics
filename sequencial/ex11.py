#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   o produto do dobro do primeiro com metade do segundo .
#   a soma do triplo do primeiro com o terceiro.
#   o terceiro elevado ao cubo.

num1 = input("Informe o primeiro numero inteiro: ")
num_1 = float(num1)

num2 = input("Informe o segundo numero inteiro: ")
num_2 = float(num2)

num3 = input("Informe o numero real: ")
num_3 = float(num3)

first = (num_1 * 2) * (num_2/2)

second = (num_1 * 3) + num_3

third = (num_3 * num_3 * num_3)

print(first)

print(second)

print(third)




