#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print("Informe uma data no formato dd/mm/aaaa" )
dias_str = input("Primeiro os dias: ")
dias = int(dias_str)

meses_str = input("Agora o mês: ")
meses = int(meses_str)

anos_str = input("Agora o ano: ")
anos = int(anos_str)

if((dias > 0 and dias < 31) and (meses > 0 and meses < 13) and anos < 2022):
    print("Data válida")
else:
    print("Data não válida")