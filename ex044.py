"""
Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
print(f"{' Carrinho de compras ':=^40}")  # Formata "Carrinho de compras centralizado em 40 espaços e adiciona "=" nos vazios
total = float(input("Preço das compras: R$"))
i = 0
while i == 0:
    print("ESCOLHA A FORMA DE PAGAMENTO\n"
          "[ 1 ] à vista - dinheiro/cheque\n"
          "[ 2 ] à vista - cartão\n"
          "[ 3 ] 2x no cartão\n"
          "[ 4 ] 3x ou mais no cartão")
    op = int(input("Como deseja pagar? "))
    if op == 1 or op == 2:
        if op == 1:
            desc = 0.1
            jur = 0
            op = "à vista com dinheiro ou cheque"
            i = 1
        elif op == 2:
            desc = 0.05
            op = "à vista no cartão"
            i = 1
        print(f"Você optou por pagar {op} e irá receber {int(desc * 100)}% de desconto.")
        print(f"Sua compra no valor de R${total:.2f} sairá por R${total * (1 - desc):.2f}.")
    elif op == 3:
        op = "em 2 vezes no cartão"
        print(f"Você optou por pagar sua compra de R${total:.2f} {op}.")
        i = 1
    elif op == 4:
        desc = 0.2
        op = "em 3x ou mais no cartão"
        print(f"Você optou por pagar {op} e incidirá um juros de {int(desc * 100)}%.")
        print(f"Sua compra no valor de R${total:.2f} sairá por R${total * (1 + desc):.2f}.")
        i = 1
    else:
        print("\nNão identifiquei a sua forma de pagamento...\nVamos repetir?\n")
