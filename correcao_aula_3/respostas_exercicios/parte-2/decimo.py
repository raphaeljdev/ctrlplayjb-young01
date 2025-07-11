user1 = input("Cadastre o nome do usuário 1: ")
pass1 = input("Cadastre a senha do usuário 1: ")
user2 = input("Cadastre o nome do usuário 2: ")
pass2 = input("Cadastre a senha do usuário 2: ")

login = input("Nome de usuário para login: ")
senha = input("Senha para login: ")

if login == user1 and senha == pass1:
    print(f"Bem-vindo, {user1}!")
elif login == user2 and senha == pass2:
    print(f"Bem-vindo, {user2}!")
else:
    print("Usuário ou senha incorretos.")
