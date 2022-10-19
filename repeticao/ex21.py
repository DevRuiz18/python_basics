#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Informe um numero para verificar se ele é primo: "))
count = 0
for i in range(1, num+1):
        if(num%i == 0):
            count += 1
if(count == 2):
    print("O numero é primo!")
else:
    print("O numero não é primo")