#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno_str = input("Conforme M-matutino ou V-Vespertino ou N- Noturno. Em qual turno você estuda: ")

if(turno_str == "M" or turno_str == "m"):
    print("Bom Dia!")
elif(turno_str == "V" or turno_str == "v"):
    print("Boa Tarde!")
elif(turno_str == "N" or turno_str == "n"):
    print("Boa Noite!")
else:
    print("Valor Inválido!")