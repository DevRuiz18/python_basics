#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! =  5 . 4 . 3 . 2 . 1 = 120

num = int(input("Informe o numero que deseja calcular o fatorial: "))
factorial = 1

for i in range(1, num+1):
    factorial = factorial * i
    print(factorial)

print("Fatorial de: {}".format(num))
print("{}! = ".format(num), end="")

for i in range(1, num+1):
    print("{}.".format(num+1 -i), end="")

print(" = {}".format(factorial))
