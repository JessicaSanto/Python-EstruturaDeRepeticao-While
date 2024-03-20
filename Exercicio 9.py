#Faça um programa que solicite ao usuário números indefinidamente até que ele digite 0. Em seguida, o programa deve imprimir a média dos números digitados.

soma = 0
quantidade = 0

# Loop infinito, que será interrompido quando o usuário digitar 0
while True:
    numero = float(input("Digite um numero qualquer e 0 para sair: "))

    # Se o número digitado for 0, o loop é interrompido
    if numero == 0:
        break

    # Se o número digitado for diferente de 0, ele é adicionado à soma e a contagem é incrementada
    soma += numero
    quantidade += 1

# Se a quantidade de números digitados for maior que 0, calcula a média e a apresenta
if quantidade > 0:
    media = soma / quantidade
    print(f"A média dos numeros digitados é {media}")
else:
    # Se nenhum número foi digitado, informa ao usuário
    print("nenhum numero foi digitado")
