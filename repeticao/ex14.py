#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

num = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10):
    num[i] = int(input("Informe um numero para posição {}: ".format(i+1)))

pair_count = 0
odd_count = 0

for i in range(10):
    if(num[i]%2 == 0):
        pair_count += 1
    else:
        odd_count += 1

print("Nos 10 numero informados tiveram {} numeros pares e {} numeros impares.".format(pair_count, odd_count))

