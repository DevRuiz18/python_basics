#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
#continue pedindo até que o usuário informe um valor válido.

while(1 == 1):
    grade = float(input("Informe a nota do aluno: "))
    if(grade < 0 or grade < 10):
        print("Nota dentro dos conformes")
        break