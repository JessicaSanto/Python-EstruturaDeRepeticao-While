# - [ ]  Faça um programa que leia e valide as seguintes informações:
# - Nome: maior que 3 caracteres;
# - Idade: entre 0 e 150;
# - Salário: maior que zero;
# - Sexo: 'f' ou 'm';
# - Estado Civil: 's', 'c', 'v', 'd';

# Solicita ao usuário inserir o nome completo e valida se tem mais de 3 caracteres
nome = input("Digite o seu nome completo: ")
while len(nome) <= 3:
    nome = input("O nome precisa ter mais que 3 caracteres, digite o seu nome novamente: ")

# Solicita ao usuário inserir a idade e valida se está entre 0 e 150
idade = int(input("Digite a sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida, Digite novamente a sua idade: "))

# Solicita ao usuário inserir o salário e valida se é maior que zero
salario = float(input("Digite o seu salário: "))
while salario <= 0:
    salario = float(input("Seu pobre!! Tenha mais que 0 na sua conta, digite novamente: "))

# Solicita ao usuário inserir o sexo e valida se é 'f' ou 'm'
sexo = input("Digite o seu sexo [f, m]: ")
while sexo != 'f' and sexo != 'm':
    sexo = input("Opção inválida!! Digite o seu sexo novamente [f, m]: ")

# Solicita ao usuário inserir o estado civil e valida se é 's', 'c', 'v' ou 'd'
estado_civil = input("Digite o seu estado civil [s = solteiro; c = casado; v = viúvo; d = divorciado]: ")
while estado_civil not in ['s', 'c', 'v', 'd']:
    estado_civil = input("Entrada inválida!! Digite o seu estado civil novamente [s = solteiro; c = casado; v = viúvo; d = divorciado]: ")
