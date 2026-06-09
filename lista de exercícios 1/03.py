nome = input("Insira o seu nome de usuario: ")
senha = input("Insira sua senha: ")
if nome == "admin":
    if senha == "12345":
        print("Login bem-secedido!")
    else:
        print("Nome de usuário ou senha incorretos.")
else:
    print("Nome de usuário ou senha incorretos.")