#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e
#limitando o fatorial a números inteiros positivos e menores que 16.

gtg = False
ntg = False

while(gtg == False):
    while(ntg == False):
        num = int(input("Informe o numero q deseja calcular o faotrial: "))
        if(num > 16):
            print("Numero excedeu os limites suportados, por favor informe outro numero: ")
        else:
            ntg = True


    sum = 1

    for i in range(1, num+1):
        sum *= i
    print("O fatorial de {} é {}".format(num, sum))

    decision = input("Deseja realizar outra conta ?: ")
    if(decision == "N" or decision == "n"):
        gtg = True
        print("Obrigado por usar o programa!")


