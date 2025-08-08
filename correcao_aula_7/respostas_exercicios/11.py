def fatorial(n):
  """Calcula o fatorial de n usando recursão."""
  # Caso base: fatorial de 0 ou 1 é 1.
  if n == 0 or n == 1:
    return 1
  # Passo recursivo: n * fatorial(n-1)
  else:
    return n * fatorial(n - 1)

# Chamando a função
numero = 5
print(f"O fatorial de {numero} é {fatorial(numero)}")