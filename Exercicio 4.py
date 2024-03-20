#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

# [ok]Faça um programa que leia um nome de usuário
# [ok]Faça um programa que leia a senha de usuário
# [ok]não aceite a senha igual ao nome do usuário
# [ok]mostrando uma mensagem de erro
# [ok]voltar a pedir as infos

# Solicita ao usuário inserir o nome de usuário
nome = input("Digite o seu nome de usuário: ")

# Solicita ao usuário inserir a senha
senha = input("Digite sua senha: ")

# Inicia um loop enquanto a senha for igual ao nome de usuário
while senha == nome:
    # Imprime uma mensagem de erro informando que a senha não pode ser igual ao nome de usuário
    print("ERRO! A senha não pode ser igual ao nome do usuário!")
    # Solicita ao usuário inserir novamente o nome de usuário
    nome = input("Digite o seu nome de usuário: ")
    # Solicita ao usuário inserir novamente a senha
    senha = input("Digite sua senha: ")
