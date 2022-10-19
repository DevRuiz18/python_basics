#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num_1 = input("Informe um número: ")
num1 = int(num_1)

if((num1%2) != 0):
    print("O número é impar")
else:
    print("O número é par")