def tabuada(numero):
  """Imprime a tabuada de um número, do 1 ao 10."""
  print(f"--- Tabuada do {numero} ---")
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Chamando a função
tabuada(7)