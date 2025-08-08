def contar_vogais(texto):
  """Conta o número de vogais em uma string."""
  vogais = "aeiou"
  contador = 0
  for letra in texto.lower(): # .lower() para não diferenciar maiúsculas
    if letra in vogais:
      contador += 1
  return contador

# Chamando a função
frase = "Python é Incrível"
print(f"A frase '{frase}' tem {contar_vogais(frase)} vogais.")