#Faça um programa que calcule o número médio de alunos por turma.
#Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

n = int(input("Informe quantas turmas serão contadas: "))
x = 1
students_sum = 0
for i in range(n):
    x = 1
    while x == 1:
        students = int(input("Informe quantos estudantes tem na turma: "))
        if (students > 0 and students <= 40):
            x -= 1
        else:
            print("O limite de alunos é 40.")
    students_sum += students
print("A média de alunos por turma é {}".format(students_sum/n))
