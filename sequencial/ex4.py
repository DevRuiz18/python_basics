#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = input("Informe a primeira nota do aluno: ")
nota2 = input("Informe a segunda nota do aluno: ")
nota3 = input("Informe a terceira nota do aluno: ")
nota4 = input("Informe a quarta nota do aluno: ")

media = (int(nota1) + int(nota2) + int(nota3) + int(nota4)) / 4

print("A média do aluno é:", media)