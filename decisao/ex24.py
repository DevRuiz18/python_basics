#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#   par ou ímpar;
#   positivo ou negativo;
#   inteiro ou decimal.

num = float(input("informe um numero para extrair dados dele: "))

print("O numero", num, "é:")

if(num % 2 == 0):
    print("→ Par;")
    if(num > 0):
        print("→ Positivo;")
    else:
        print("→ Negativo;")
    if (num % 1 == 0):
        print("→ Inteiro.")
    else:
        print("→ Decimal.")
else:
    print("→ Impar;")
    if (num > 0):
        print("→ Positivo;")
    else:
        print("→ Negativo;")
    if (num % 1 == 0):
        print("→ Inteiro.")
    else:
        print("→ Decimal.")