#- [ ]  O cardápio de uma lanchonete é o seguinte:

#Especificação   Código  Preço
#Cachorro Quente 100     R$ 1,20
#Bauru Simples   101     R$ 1,30
#Bauru com ovo   102     R$ 1,50
#Hambúrguer      103     R$ 1,20
#Cheeseburguer   104     R$ 1,30
#Refrigerante    105     R$ 1,00

#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.

#Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.

#Considere que o cliente deve informar quando o pedido deve ser encerrado.

quantidade_produto_100 = 0
quantidade_produto_101 = 0
quantidade_produto_102 = 0
quantidade_produto_103 = 0
quantidade_produto_104 = 0
quantidade_produto_105 = 0
total = 0

# Mostra a tabela de produtos
print("""
    Produto            Codigo  Preco
    --------------------------------
    Cachorro Quente  100     R$ 1.20
    Bauru Simples    101     R$ 1.30
    Bauru com Ovo    102     R$ 1.50
    Hamburguer       103     R$ 1.20
    Cheeseburguer    104     R$ 1.30
    Refrigerante     105     R$ 1.00
"""
      )

# Loop para registrar os produtos
while True:
    codigo = int(input("Digite o codigo do produto que deseja adquirir (ou 0 para encerrar): "))

    if codigo == 0:
        break

    if codigo < 100 or codigo > 105:
        print("Código Invalido!!!")
        continue

    quantidade = int(input("Digite a quantidade desse produto: "))

    # Calcula o preço do produto e atualiza o total
    if codigo == 100:
        preco_unitario = 1.20
        quantidade_produto_100 += quantidade
    elif codigo == 101:
        preco_unitario = 1.30
        quantidade_produto_101 += quantidade
    elif codigo == 102:
        preco_unitario = 1.50
        quantidade_produto_102 += quantidade
    elif codigo == 103:
        preco_unitario = 1.20
        quantidade_produto_103 += quantidade
    elif codigo == 104:
        preco_unitario = 1.30
        quantidade_produto_104 += quantidade
    elif codigo == 105:
        preco_unitario = 1.00
        quantidade_produto_105 += quantidade

    # Calcula e mostra o preço total do produto
    preco_total = preco_unitario * quantidade
    print(
        f"Codigo {codigo} - Quantidade {quantidade} - Preço unidade R${preco_unitario:.2f} - Preço Total R${preco_total:.2f}")

    # Atualiza o total da compra
    total += preco_total

# Mostra o total do pedido
print(f"Total do pedido: R${total:.2f}")
