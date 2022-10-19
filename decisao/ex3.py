#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo_str = input("Conforme F - Feminino, M - Masculino, informe o sexo: ")

if(sexo_str == "F" or sexo_str == "f"):
    print("O sexo é feminino")
elif(sexo_str == "M" or sexo_str == "m"):
    print("O sexo é masculino")
else:
    print("Sexo Inválido")
