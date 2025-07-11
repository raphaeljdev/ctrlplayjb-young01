i1 = int(input("Idade 1: "))
i2 = int(input("Idade 2: "))

if i1 <= 12:
    print("Idade 1 é criança.")
elif i1 <= 17:
    print("Idade 1 é adolescente.")
elif i1 <= 59:
    print("Idade 1 é adulto.")
else:
    print("Idade 1 é idoso.")

if i2 <= 12:
    print("Idade 2 é criança.")
elif i2 <= 17:
    print("Idade 2 é adolescente.")
elif i2 <= 59:
    print("Idade 2 é adulto.")
else:
    print("Idade 2 é idoso.")
