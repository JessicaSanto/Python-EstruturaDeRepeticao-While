#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

# Define a população inicial do país A
PaisA = 80000

# Define a população inicial do país B
PaisB = 200000

# Inicializa a variável ano como zero para contar os anos necessários
ano = 0

# O loop continua enquanto a população do país B for maior ou igual à população do país A
while PaisB >= PaisA:
    # Calcula o crescimento anual da população do país A (3% de aumento)
    PaisA += PaisA * 0.03

    # Calcula o crescimento anual da população do país B (1.5% de aumento)
    PaisB += PaisB * 0.015

    # Incrementa o contador de anos
    ano += 1

# Após o loop, imprime o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B
print(f"A quantidade de anos é: {ano}")
