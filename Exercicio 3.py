#Um funcionário de uma empresa recebe aumento salarial anualmente.

#Sabe-se que:
#Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
#dobro do percentual do ano anterior.

#Faça um programa que determine o salário atual desse funcionário.
#Após concluir isto, altere o programa permitindo que o usuário digite o salário
#inicial do funcionário.

# Solicita ao usuário inserir o salário inicial do funcionário
salario = float(input("Digite um salario: "))

# Define o ano inicial como 1995
ano = 1995

# Solicita ao usuário inserir o ano atual
ano_atual = int(input("Digite o ano em que estamos: "))

# Define o percentual inicial de aumento
aumento = 1.5 / 100

# Inicia um loop para calcular o salário para cada ano até o ano atual
while ano < ano_atual:
    # Incrementa o ano em 1 para o próximo ano
    ano += 1
    # Calcula o novo salário com base no aumento percentual
    salario = salario * (1 + aumento)
    # Dobrar o aumento percentual para o próximo ano
    aumento *= 2
    # Imprime o salário para o ano atual
    print(f"O salario em {ano} é de R$ {salario:.2f}")
