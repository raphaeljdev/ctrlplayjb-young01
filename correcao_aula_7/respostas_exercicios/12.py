def validar_senha(senha):
  """Valida uma senha com base em critérios de segurança."""
  tem_maiuscula = False
  tem_minuscula = False
  tem_numero = False
  
  # 1. Critério de comprimento
  if len(senha) < 8:
    return False
  
  # 2. Critérios de conteúdo
  for char in senha:
    if char.isupper():
      tem_maiuscula = True
    elif char.islower():
      tem_minuscula = True
    elif char.isdigit():
      tem_numero = True
      
  return tem_maiuscula and tem_minuscula and tem_numero

# Testando a função
print(f"Senha 'senhafraca': {validar_senha('senhafraca')}")
print(f"Senha 'SenhaForte123': {validar_senha('SenhaForte123')}")
print(f"Senha 'SENHAFORTE': {validar_senha('SENHAFORTE')}")