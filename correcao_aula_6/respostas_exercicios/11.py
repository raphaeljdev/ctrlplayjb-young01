cadastro = {
    "RA123": {"nome": "Ana", "notas": (7.0, 8.5)},
    "RA456": {"nome": "Bruno", "notas": (9.0, 6.5)},
    "RA789": {"nome": "Carla", "notas": (5.0, 6.0)}
}

ra_digitado = input("Digite o RA do aluno: ")

if ra_digitado in cadastro:
    aluno = cadastro[ra_digitado]       # Pega o dicionário do aluno
    nome_aluno = aluno["nome"]          # Pega o nome
    notas_aluno = aluno["notas"]        # Pega a tupla de notas
    
    media = (notas_aluno[0] + notas_aluno[1]) / 2
    
    print(f"Aluno: {nome_aluno}")
    print(f"Média: {media}")
else:
    print("Aluno não encontrado.")