def eh_primo(num):
  """Função auxiliar que verifica se um número é primo."""
  if num < 2:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def primos_ate_n(n):
  """Retorna uma lista de todos os números primos até n."""
  lista_primos = []
  for numero in range(2, n + 1):
    if eh_primo(numero): # Usa a função auxiliar
      lista_primos.append(numero)
  return lista_primos

# Chamando a função principal
limite = 30
print(f"Números primos até {limite}: {primos_ate_n(limite)}")