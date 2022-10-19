#Encontrar números primos é uma tarefa difícil.
# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

num = int(input("Informe um numero para gerarmos a lista de todos os numeros primos no intervalo de 1 e ele: "))
count = 0
print("Inicio da fila:")
for j in range (1, num+1):
    count = 0
    for i in range(1, j+1):
        if(j%i == 0):
            count= count + 1

    if(count == 2):
        print("O numero {} é primo.".format(j))
    else:
        print("O numero {} não é primo.".format(j))

print("Fim da lista.")