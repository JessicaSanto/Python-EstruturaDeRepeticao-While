#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

# Inicializa as variáveis para os dois primeiros termos da sequência de Fibonacci
ultimo = 1
penultimo = 1
cont = 1

# Imprime os dois primeiros termos da sequência
print(ultimo)
print(penultimo)

# Loop para gerar os próximos 8 termos da sequência de Fibonacci
while cont <= 9:
    # Calcula o próximo termo da sequência somando os dois últimos termos
    termo = ultimo + penultimo

    # Atualiza os dois últimos termos para os próximos cálculos
    penultimo = ultimo
    ultimo = termo

    # Incrementa o contador
    cont += 1

    # Imprime o termo atual da sequência
    print(termo)
