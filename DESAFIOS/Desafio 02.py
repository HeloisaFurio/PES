import subprocess

nome = input("Digite seu nome de usuario do Github: ")
email = input("Digite seu e-mail: ")

subprocess.run(["git", "config", "--global", "user.name", nome])
subprocess.run(["git", "config", "--global", "user.email", email])

print("Configuração do Git aplicada com sucesso!")
