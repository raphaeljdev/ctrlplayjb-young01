# Sistema simples de notas

nota = float(input("Digite sua nota (0 a 10): "))

if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")
