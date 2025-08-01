notas_alunos = {"Ana": 9.5, "Bruno": 7.0, "Carla": 8.5, "Daniel": 7.5}

maior_nota = -1.0  # Começa com um valor impossível de ser uma nota
nome_melhor_aluno = ""

for nome, nota in notas_alunos.items():
    if nota > maior_nota:
        maior_nota = nota
        nome_melhor_aluno = nome

print(f"O aluno com a maior nota é '{nome_melhor_aluno}' com a nota {maior_nota}.")