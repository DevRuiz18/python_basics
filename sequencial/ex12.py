#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# (72.7*altura) - 58

alt_ = input("Informe sua altura: ")
alt = float(alt_)

peso_ideal = (72.7 * alt) - 58

print("O peso ideal da é", peso_ideal)