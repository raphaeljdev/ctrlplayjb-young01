def pode_votar(idade):
  """Verifica se a pessoa pode votar com base na idade."""
  if idade >= 16:
    return "Pode votar"
  else:
    return "Não pode votar"

# Chamando a função
print(f"Com 18 anos? {pode_votar(18)}")
print(f"Com 15 anos? {pode_votar(15)}")