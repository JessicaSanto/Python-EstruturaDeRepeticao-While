#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

# Solicita ao usuário inserir um número inteiro para calcular o fatorial
numero = int(input("Digite um numero inteiro para saber o fatorial: "))

# Inicializa o contador para 1 e o fatorial para 1 (pois o fatorial de 0 e 1 é 1)
cont = 1
fatorial = 1

# O loop continua enquanto o contador for menor ou igual ao número inserido
while cont <= numero:
    # Calcula o fatorial multiplicando o fatorial atual pelo valor do contador
    fatorial = fatorial * cont

    # Incrementa o contador para avançar para o próximo número no cálculo do fatorial
    cont += 1

# Após o loop, imprime o valor do fatorial calculado
print(fatorial)
