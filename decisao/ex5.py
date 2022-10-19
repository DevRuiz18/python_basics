#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#   A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#   A mensagem "Reprovado", se a média for menor do que sete;
#   A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1_str =  input("Informe a primeira nota do aluno: ")
nota1 = int(nota1_str)

nota2_str =  input("Informe a segunda nota do aluno: ")
nota2 = int(nota2_str)

media = (nota1 + nota2) / 2

if(media >= 7):
    print("O aluno foi aprovado")
    if(media == 10):
        print("E obteve a nota maxima!")
else:
    print("O aluno foi reprovado")