#- Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
#Os códigos utilizados são:
#1, 2, 3, 4  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#5 - Voto Nulo
#6 - Voto em Branco

#Faça um programa que calcule e mostre:
#O total de votos para cada candidato;
#O total de votos nulos;
#O total de votos em branco;
#A percentagem de votos nulos sobre o total de votos;
#A percentagem de votos em branco sobre o total de votos.
#Para finalizar o conjunto de votos tem-se o valor zero.

print("Candidatos: \n1 - Pericles\n2 - Sosia do Pelé\n3 - Zeca Pagodinho\n4 - Hulk Magrelo ")
print("Digite 0 para sair, 5 para votar nulo ou 6 para votar em branco")

# Inicializa as variáveis para contagem dos votos
votos = 0
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
nulos = 0
brancos = 0

# Loop para registrar os votos
while True:
    # Solicita o voto ao usuário
    voto = int(input(f"Digite o voto numero {votos + 1}: "))

    # Verifica se o voto é para sair do loop
    if voto == 0:
        break

    # Incrementa o número total de votos
    votos += 1

    # Contabiliza o voto para o candidato correspondente
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    elif voto == 4:
        candidato_4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Voto Invalido")
        votos -= 1

# Mostra o resultado da eleição
print(f"""
    Resultado da Eleição:
    Pericles teve {candidato_1} votos
    Sosia do Pelé teve {candidato_2} votos
    Zeca Pagodinho teve {candidato_3} votos
    Hulk Magrelo teve {candidato_4} votos
    {nulos} votos foram anulados, um total de {100 * nulos / votos:.2f}%
    {brancos} votos foram em branco, um total de {100 * brancos / votos:.2f}%
""")
