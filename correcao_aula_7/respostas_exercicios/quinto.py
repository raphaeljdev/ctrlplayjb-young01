def calcular_area(largura=1, altura=1):
  """Calcula a área de um retângulo com valores padrão."""
  return largura * altura

# Testando a função
print(f"Área 1 (5x10): {calcular_area(5, 10)}")
print(f"Área 2 (7): {calcular_area(7)}") # altura usará o padrão 1
print(f"Área 3 (padrão): {calcular_area()}") # usará largura=1 e altura=1