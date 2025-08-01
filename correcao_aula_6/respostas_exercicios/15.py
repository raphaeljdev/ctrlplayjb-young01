votos = {"Candidato A": 0, "Candidato B": 0, "Candidato C": 0}

print("--- Urna Eletrônica ---")
print("Candidatos disponíveis: Candidato A, Candidato B, Candidato C")

while True:
    voto = input("Digite o nome do seu candidato (ou 'fim' para encerrar): ")

    if voto.lower() == 'fim':
        break

    if voto in votos:
        votos[voto] += 1
        print("Voto computado!")
    else:
        print("Candidato inválido! Tente novamente.")

print("\n--- Resultado Final da Votação ---")
for candidato, total_votos in votos.items():
    print(f"{candidato}: {total_votos} votos")