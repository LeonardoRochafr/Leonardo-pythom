nome_usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

while nome_usuario == senha:
    print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
    senha = input("Digite sua senha: ")

print("Cadastro efetuado com sucesso!")
