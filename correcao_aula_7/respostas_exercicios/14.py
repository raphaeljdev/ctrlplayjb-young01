def calcular_media_ponderada(notas, pesos):
  """Calcula a média ponderada a partir de dicionários de notas e pesos."""
  soma_notas_pesos = 0
  soma_pesos = 0
  
  for materia in notas:
    # Garante que a matéria tem tanto nota quanto peso
    if materia in pesos:
      soma_notas_pesos += notas[materia] * pesos[materia]
      soma_pesos += pesos[materia]
      
  # Evita divisão por zero se não houver pesos
  if soma_pesos == 0:
    return 0
    
  return soma_notas_pesos / soma_pesos

# Testando a função
notas_aluno = {"Cálculo": 8.5, "Física": 9.0, "Química": 7.0}
pesos_materias = {"Cálculo": 3, "Física": 2, "Química": 1}

media = calcular_media_ponderada(notas_aluno, pesos_materias)
print(f"A média ponderada do aluno é: {media:.2f}")