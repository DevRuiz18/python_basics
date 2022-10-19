#Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
#   Código da cidade;
#   Número de veículos de passeio (em 1999);
#   Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
#   Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
#   Qual a média de veículos nas cinco cidades juntas;
#   Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cod_cidade = []
num_veiculos = []
num_vitimas = []

for i in range(0,5):
    cod =  int(input("Informe o código da cidade {}: ".format(i+1)))
    veiculos = int(input("Informe o numero de veiculos para a cidade {}: ".format(i+1)))
    vitimas = int(input("Informe o numero de acidentes para a cidade {}: ".format(i+1)))

    cod_cidade.append(cod)
    num_veiculos.append(veiculos)
    num_vitimas.append(vitimas)

maior_indice = num_vitimas.index(max(num_vitimas))
menor_indice = num_vitimas.index(min(num_vitimas))

maior_indice_cod = num_vitimas.index(max(num_vitimas))
menor_indice_cod = num_vitimas.index(min(num_vitimas))

print("O maior indices de acidentes pertence a cidade {} sendo ele {}.".format(cod_cidade[maior_indice_cod], num_vitimas[maior_indice]))
print("O menor indices de acidentes pertence a cidade {} sendo ele {}.".format(cod_cidade[menor_indice_cod], num_vitimas[menor_indice]))

print("A média de carros pelas cidades são: {}".format(sum(num_veiculos)/len(cod_cidade)))

