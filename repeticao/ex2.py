#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.


while(1 == 1):
    user_name_str = input("Informe seu nome: ")
    password = input("Informe sua senha: ")

    if(user_name_str != password):
        print("Os padrões para a senha e nome de usuário foram atendidos!")
        break
    else:
        print("Algo esta errado, tente novamente: \n")