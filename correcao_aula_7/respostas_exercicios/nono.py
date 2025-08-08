def aplicar_desconto(preco_original, percentagem_desconto):
  """Calcula o novo preço após aplicar um desconto percentual."""
  desconto = preco_original * (percentagem_desconto / 100)
  novo_preco = preco_original - desconto
  return novo_preco

# Chamando a função
preco = 150.00
desconto = 20 # 20%
print(f"Preço original: R${preco:.2f}")
print(f"Novo preço com {desconto}% de desconto: R${aplicar_desconto(preco, desconto):.2f}")