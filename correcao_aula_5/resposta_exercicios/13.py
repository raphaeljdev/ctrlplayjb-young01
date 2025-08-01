numero_secreto = 42
max_tentativas = 5
acertou = False

print("Jogo de Adivinhação! Tente adivinhar o número secreto entre 1 e 100.")

for tentativa in range(1, max_tentativas + 1):
    print(f"--- Tentativa {tentativa} de {max_tentativas} ---")
    palpite = int(input("Qual é o seu palpite? "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        acertou = True
        break
    elif palpite < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")

if not acertou:
    print(f"\nFim de jogo! Você não conseguiu adivinhar. O número era {numero_secreto}.")   