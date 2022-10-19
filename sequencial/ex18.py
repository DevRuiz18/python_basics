#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tam_arquivo_str = input("Informe quantos MB tem o arquivo que deseja baixar: ")
tam_arquivo = int(tam_arquivo_str)

vel_internet_str = input("Iforme a velocidade da internet em MBps: ")
vel_internet = int(vel_internet_str)

qntd_segundos = tam_arquivo / vel_internet

qntd_minutos = qntd_segundos / 60

print("Levará", int(qntd_minutos), "minutos para baixar")