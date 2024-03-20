#1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# [ok] Faça um programa que peça uma nota, entre zero e dez.
# [ok]Mostre uma mensagem caso o valor seja inválido
# [OK]Testar Valor
# [ok]Continue pedindo até que o usuário informe um valor válido.

# Solicita ao usuário inserir uma nota e a converte em um número de ponto flutuante (float)
nota = float(input("Digite uma nota apenas entre zero e dez: "))

# Inicia um loop enquanto a nota inserida estiver fora do intervalo válido (0 a 10)
while nota > 10 or nota < 0:
    # Se a nota for inválida, imprime uma mensagem de erro e solicita ao usuário que insira novamente uma nota válida
    nota = float(input("VALOR INVALIDO!!!! Informe novamente a nota, com um valor valido: "))
