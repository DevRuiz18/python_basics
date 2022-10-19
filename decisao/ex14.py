#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#     Média de Aproveitamento  Conceito
#     Entre 9.0 e 10.0        A
#     Entre 7.5 e 9.0         B
#     Entre 6.0 e 7.5         C
#     Entre 4.0 e 6.0         D
#     Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1_str = input("Informe a primeira nota do aluno: ")
nota1 = float(nota1_str)

nota2_str = input("Informe a segunda nota do aluno: ")
nota2 = float(nota2_str)

media = (nota1 + nota2) / 2

if(media > 9  and media <= 10):
    print("O teve as notas  :", nota1, "e", nota2)
    print("A média          :", media)
    print("Conceito         : A")
    print("O aluno foir APROVADO!")
elif(media > 7.5  and media <= 9):
    print("O teve as notas  :", nota1, "e", nota2)
    print("A média          :", media)
    print("Conceito         : B")
    print("O aluno foir APROVADO!")

elif(media > 6  and media <= 7.5):
    print("O teve as notas  :", nota1, "e", nota2)
    print("A média          :", media)
    print("Conceito         : C")
    print("O aluno foir APROVADO!")

elif(media > 4  and media <= 6):
    print("O teve as notas  :", nota1, "e", nota2)
    print("A média          :", media)
    print("Conceito         : D")
    print("O aluno foir REPROVADO!")

else:
    print("O teve as notas  :", nota1, "e", nota2)
    print("A média          :", media)
    print("Conceito         : E")
    print("O aluno foir REPROVADO!")