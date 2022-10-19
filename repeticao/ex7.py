#Faça um programa que leia 5 números e informe o maior número.

num = [0, 0, 0, 0, 0]
bigger = -9999999


for i in range(5) :
    num[i] = int(input("informe o {} numero: ".format(i+1)))

for j in range(5):
    if (bigger < num[j]):
        bigger = num[j]

print("O maior numero é : {}".format(bigger))