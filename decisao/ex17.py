#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano_str = input("Informe um ano e te falaremos se ele é bissexto: ")
ano = int(ano_str)

if(ano%4 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")