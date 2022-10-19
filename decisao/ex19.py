#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#   326 = 3 centenas, 2 dezenas e 6 unidades
#   12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

num_str = input("Informe um número inteiro menor que 1000: ")
num = int(num_str)

centena = num - num%100
qnt_centena = centena / 100

dezena = num - (qnt_centena * 100)
qnt_dezena = dezena / 10

unidades = num - (qnt_centena * 100) - (int(qnt_dezena) * 10)



print("Centena(s)   :", int(qnt_centena))
print("Dezena(s)    :", int(qnt_dezena))
print("Unidade(s)   :", int(unidades))
