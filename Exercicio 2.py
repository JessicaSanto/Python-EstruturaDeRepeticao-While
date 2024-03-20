#Faça um programa que calcule o mostre a média aritmética de N notas.

# Inicializa as variáveis notas, contador e continuar
notas = 0
contador = 0
continuar = "S"

# Inicia um loop que continua enquanto o usuário desejar continuar inserindo notas
while continuar == "S":
    # Solicita ao usuário inserir uma nota e a converte em um número de ponto flutuante
    nota = float(input("Digite uma nota: "))
    # Incrementa a variável notas com o valor da nota inserida
    notas += nota
    # Incrementa o contador de notas
    contador += 1
    # Pergunta ao usuário se deseja continuar inserindo notas
    continuar = input("Deseja Continuar? Sim(S) ou qualquer tecla para sair: ").upper()

# Calcula a média das notas dividindo a soma das notas pelo total de notas inseridas
media = notas / contador

# Imprime a média das notas com duas casas decimais
print(f"A média das notas é {media:.2f}")
