#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

n = int(input("Informe o numero de pessoas que vão votar: "))
candidate1_sum = 0
candidate2_sum = 0
candidate3_sum = 0

for i in range(n):
    vote = int(input("Informe em qual candidato deseja votar [1]- Jão, [2]- Pedro e [3]- Bitola: "))
    if(vote == 1):
        candidate1_sum += 1
    elif(vote == 2):
        candidate2_sum += 1
    else:
        candidate3_sum += 1

print("O votos por cadidato foram: ")
print("Candidato 1 - {}.".format(candidate1_sum))
print("Candidato 2 - {}.".format(candidate2_sum))
print("Candidato 3 - {}.".format(candidate3_sum))