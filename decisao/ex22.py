#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

num_str = input("Informe um número: ")
num = int(num_str)

if(num%2 == 0):
    print("O número é par")
else:
    print("O número é impar")
