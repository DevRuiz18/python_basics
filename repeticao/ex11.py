#Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input("Informe o primeiro numero inteiro: "))

num2 = int(input("Informe o segundo numero inteiro: "))

sum = 0

if(num2 > num1):
    for i in range(num1+1, num2):
        print(i)
        sum += i
else:
    print("Da proxima vez informa o segundo numero maior que o primeiro!")

print("A soma dos numeros no intervalo de {} a {}, é: {}".format(num1, num2, sum))