#- [ ]  O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
#Faça um programa que implemente uma caixa registradora rudimentar.
#O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra.

#O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.
#A saída deve ser conforme o exemplo abaixo:
#Lojas Tabajara
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00

print("Lojas Tabajara")  # Mensagem inicial

total = 0  # Inicializa o total da compra
produto = 0  # Inicializa o contador de produtos
valor = 0  # Inicializa o valor do produto

while True:  # Loop infinito para registrar as compras
    produto += 1  # Incrementa o contador de produtos
    valor = float(input(f"Produto {produto}: R$"))  # Solicita o preço do próximo produto

    total += valor  # Adiciona o valor do produto ao total da compra

    if valor == 0:  # Verifica se o valor digitado é zero, indicando o final da compra
        produto = 0  # Reinicia o contador de produtos para a próxima compra
        valor = 0  # Reinicia o valor do produto para a próxima compra

        # Exibe o total da compra
        print(f"O Total da compra foi R${total:.2f}")

        # Solicita o valor em dinheiro fornecido pelo cliente
        dinheiro = float(input("Dinheiro Recebido: R$"))

        # Calcula o troco
        troco = dinheiro - total

        # Exibe o valor do troco
        print(f"Troco: {troco:.2f}")

        total = 0  # Reinicia o total da compra para a próxima compra
        print("Lojas Tabajara")  # Mensagem indicando o início de uma nova compra
