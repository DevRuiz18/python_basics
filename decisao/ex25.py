#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#       "Telefonou para a vítima?"
#       "Esteve no local do crime?"
#       "Mora perto da vítima?"
#       "Devia para a vítima?"
#       "Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
#entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("Você como suspeito passará por um teste, por obrigação com a lei responda com honestidade!")

count = 0

answer1_str = input("Você telefonou para a vítima? Pressione [S] para sim e [N] para não.\n")
if(answer1_str == "s" or answer1_str == "S"):
    count = count + 1
    print("Obrigado pela resposta.")
elif(answer1_str == "n" or answer1_str == "N"):
    print("Obrigado pela resposta.")
else:
    print("Resposta inválida")

answer2_str = input("Você esteve no local do crime? Pressione [S] para sim e [N] para não.\n")
if(answer2_str == "s" or answer2_str == "S"):
    count = count + 1
    print("Obrigado pela resposta.")
elif(answer2_str == "n" or answer2_str == "N"):
    print("Obrigado pela resposta.")
else:
    print("Resposta inválida")

answer3_str = input("Você mora perto da vítima? Pressione [S] para sim e [N] para não.\n")
if(answer3_str == "s" or answer3_str == "S"):
    count = count + 1
    print("Obrigado pela resposta.")
elif(answer3_str == "n" or answer3_str == "N"):
    print("Obrigado pela resposta.")
else:
    print("Resposta inválida")

answer4_str = input("Você devia para a vítima? Pressione [S] para sim e [N] para não.\n")
if(answer4_str == "s" or answer4_str == "S"):
    count = count + 1
    print("Obrigado pela resposta.")
elif(answer4_str == "n" or answer4_str == "N"):
    print("Obrigado pela resposta.")
else:
    print("Resposta inválida")

answer5_str = input("Você já trabalhou com a vítima? Pressione [S] para sim e [N] para não.\n")
if(answer5_str == "s" or answer5_str == "S"):
    count = count + 1
    print("Obrigado pela resposta.")
elif(answer5_str == "n" or answer5_str == "N"):
    print("Obrigado pela resposta.")
else:
    print("Resposta inválida")

print("Obrigado pelas repostas, agora computaremos uma solução para este crime!")
print("Você é: ")

if(count == 0 or count == 1):
    print("Inocente")
elif(count == 2):
    print("Suspeito")
elif(count == 3 or count == 4):
    print("Cúmplice")
elif(count == 5):
    print("Assassino")
else:
    print("Houve algum problema, por favor refaça o teste")

