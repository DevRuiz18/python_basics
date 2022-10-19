#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.
#Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

cod_aluno = []
altura_aluno = []

for i in range(0, 10):
    print("Para o {} aluno, de 10 no total. Informe ".format(i+1))
    numero = int(input("O numero do aluno: "))
    altura = float(input("A altura do aluno: "))

    cod_aluno.append(numero)
    altura_aluno.append(altura)

maior_altura_cod = altura_aluno.index(max(altura_aluno))
menor_altura_cod = altura_aluno.index(min(altura_aluno))

maior_altura = altura_aluno.index(max(altura_aluno))
menor_altura = altura_aluno.index(min(altura_aluno))

print("O aluno de numero {} possui a maior altura sendo essa de {}".format(cod_aluno[maior_altura_cod], altura_aluno[maior_altura]))
print("O aluno de numero {} possui a menor altura sendo essa de {}".format(cod_aluno[menor_altura_cod], altura_aluno[menor_altura]))
