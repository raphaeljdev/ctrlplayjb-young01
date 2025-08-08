import random

def simular_jogo():
  """Simula o lançamento de dois dados e verifica o resultado."""
  dado1 = random.randint(1, 6)
  dado2 = random.randint(1, 6)
  soma = dado1 + dado2
  
  print(f"Dados lançados: {dado1} e {dado2}. Soma: {soma}")
  
  if soma in [7, 11]:
    print("Você ganhou!")
  elif soma in [2, 3, 12]:
    print("Você perdeu!")
    
  return (dado1, dado2, soma)

# Chamando a função
print("\n--- Simulação do Jogo ---")
resultado_rodada = simular_jogo()
print(f"A função retornou a tupla: {resultado_rodada}")