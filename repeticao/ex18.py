#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

big = -999999999999999999
small = 99999999999999999
num = int(input("Informe quantos numeros deseja comparar: "))
sum = 0

for i in range(num):
    num_comp = int(input("Informe o {} numero:".format(i+1)))
    x = num_comp
    sum += x
    if(x > big):
        big = x
    if(small > x):
        small = x

print("maior: {} "
      "menor: {} "
      "soma: {}".format(big, small, sum))