#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("Informe o primeiro numero inteiro: "))

num2 = int(input("Informe o segundo numero inteiro: "))

if(num2 > num1):
    for i in range(num1+1, num2):
        print(i)
else:
    print("Da proxima vez informa o segundo numero maior que o primeiro!")