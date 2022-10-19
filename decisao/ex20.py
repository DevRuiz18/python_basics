#Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#   A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#   A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#   A mensagem "Aprovado com Distinção", se a média for igual a 10.

nota1_str = input("Informe a primeira nota do aluno: ")
nota1 = float(nota1_str)

nota2_str = input("Informe a segunda nota do aluno: ")
nota2 = float(nota2_str)

nota3_str = input("Informe a terceira nota do aluno: ")
nota3 = float(nota3_str)

media = (nota1 + nota2 + nota3) / 3

if(media >= 7):
    print("O aluno foi APROVADO!")
    if(media == 10):
        print("E o aluno tirou 10, PARABENS!")
else:
    print("O aluno foi REPROVADO!")
    