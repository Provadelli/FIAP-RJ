print("Bem vindo ao simulador de pagamento!")
valor_produto = float(input("Digite o valor do produto e pressione ENTER: "))
print("Escolha a forma de pagamento")
print("Digite 1. para pagamento à VISTA, NO PIX (10% DE DESCONTO)")
print("Digite 2. para pagamento à VISTA, NO CARTÃO DE CRÉDITO(1X)")
print("Digite 3. para pagamento PARCELADO, NO CARTÃO DE CRÉDITO(3X, COM 5% JUROS)")
pagamento = int(input("Digite uma forma de pagamento, conforme as intruções acima:"))
if pagamento == 1:
    res = valor_produto * 0.9
    print(f'Total a pagar: {res:.2f}')
elif pagamento == 2:
    res = valor_produto
    print(f'Total a pagar: {res:.2f}')
elif pagamento == 3:
    res = valor_produto / 3
    print(f"Valor das parcelas: {res:.2f}")
    res = valor_produto * 1.05
    print(f"Valor total com juros: {res:.2f}")
else:
    print("Digite uma forma de pagamento válida (1, 2, 3)")
