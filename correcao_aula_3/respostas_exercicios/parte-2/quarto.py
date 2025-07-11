n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

notas = [n1, n2]
media = (notas[0] + notas[1]) / 2

if media >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
