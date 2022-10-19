#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1_str = input("Informe o primeiro número: ")
num1 = int(num1_str)

num2_str = input("Informe o segundo número: ")
num2 = int(num2_str)

num3_str = input("Informe o terceiro número: ")
num3 = int(num3_str)

if(num2 > num1):
    if(num3 > num2 and num3 > num1):
        print(num3, num2, num1)
elif(num1 > num3):
    if(num1 > num2 and num2 > num3):
        print(num1, num3, num2)
    else:
        print(num1, num2, num3)
