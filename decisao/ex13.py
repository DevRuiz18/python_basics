#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

num_str = input("Informe o número: ")
num = int(num_str)

if(num == 1):
    print("1 -  Domingo")
elif(num == 2):
    print("2 - Segunda-Feira")
elif(num == 3):
    print("3 - Terça-Feira")
elif(num == 4):
    print("3 - Quarta-Feira")
elif(num == 5):
    print("5 - Quinta-Feira")
elif(num == 6):
    print("6 - Sexta-Feira")
elif(num == 7):
    print("7 - Sábado")
else:
    print("Número Inválido")

