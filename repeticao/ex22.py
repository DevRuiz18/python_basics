#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = int(input("Informe um numero para verificar se ele é primo: "))
count = 0
for i in range(1, num+1):
        if(num%i == 0):
            count += 1
if(count == 2):
    print("O numero é primo!")
else:
    print("O numero não é primo")
    print("Mesmo não sendo primo o numero ainda é divisivel por:")
    for i in range(1, num+1):
        if(num%i == 0):
            print(i)