p = input("Digite uma palavra de 3 letras: ")

if len(p) == 3:
    if p[0] == p[2]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")
else:
    print("A palavra deve ter 3 letras.")
