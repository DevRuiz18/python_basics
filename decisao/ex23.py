#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

num_str = input("Informe um numero: ")
num = float(num_str)

if(num%1 == 0):
    print("Inteiro")
else:
    print("Decimal")