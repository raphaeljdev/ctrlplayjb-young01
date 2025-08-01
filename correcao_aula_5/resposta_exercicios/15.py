num = int(input("Digite um número inteiro positivo para calcular o fatorial: "))
fatorial = 1

if num < 0:
    print("Não existe fatorial para números negativos.")
elif num == 0:
    print("O fatorial de 0 é 1.")
else:
    # Calcula o fatorial
    for i in range(1, num + 1):
        fatorial = fatorial * i
    print(f"O fatorial de {num} (ou {num}!) é {fatorial}")