#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1_str = input("Informe o primeiro número: ")
num1 = int(num1_str)

num2_str = input("Informe o segundo número: ")
num2 = int(num2_str)

num3_str = input("Informe o terceiro número: ")
num3 = int(num3_str)

if(num1 < num2 and num1 < num3):
    print("O primeiro número é o menor")
elif(num2 < num1 and num2 < num3):
    print("O segundo número é o menor")
else:
    print("O terceiro número é o menor")