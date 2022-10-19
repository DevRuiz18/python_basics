#Faça um programa que leia 5 números e informe a soma e a média dos números.

num = [0, 0, 0, 0, 0]
sum = 0


for i in range(5) :
    num[i] = int(input("informe o {} numero: ".format(i+1)))
    sum = sum + num[i]

print("A soma dos valores é {} e a média dos valores é {}".format(sum, sum/5))