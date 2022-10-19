#Faça um programa que leia e valide as seguintes informações:
#   Nome: maior que 3 caracteres;
#   Idade: entre 0 e 150;
#   Salário: maior que zero;
#   Sexo: 'f' ou 'm';
#   Estado Civil: 's', 'c', 'v', 'd';


while(1 == 1):
    name_str = input("Informe o seu nome: ")
    if(len(name_str) > 3):
        print("Nome dentro dos padroes")
        break
    else:
        print("Nome fora dos padrões")
print("")

while(1 == 1):
    age = int(input("Informe sua idade: "))
    if(age > 0 and age < 150):
        print("Idade valida")
        break
    else:
        print("Idade invalida")
print("")

while(1 == 1):
    wage = float(input("Informe o seu salário: "))
    if(wage > 0):
        print("Salário valido")
        break
    else:
        print("Salário invalida")
print("")

while(1 == 1):
    sex = input("Informe seu sexo comforme [F] feminino e [M] masculino: ")
    if(sex == "f" or sex == "F" or sex == "m" or sex == "M"):
        print("Sexo válido")
        break
    else:
        print("Sexo invalido")
print("")

while(1 == 1):
    sex = input("Informe seu estado civil conforme [S] solteiro, [C] casado, [V] viuvo e [D] divorciado: ")
    if(sex == "s" or sex == "S" or sex == "c" or sex == "C" or sex == "v" or sex == "V" or sex == "d" or sex == "D"):
        print("Estado civil válido")
        break
    else:
        print("Estado civil invalido")
print("")