print("Bem vindo ao Simulador de Caixa Eletrônico")
valor = int(input("Digite o valor do saque e pressione ENTER: "))
if valor < 2 or valor in [1, 3]:
    print("Erro: valor não pode ser sacado.")
else:
    notas_100 = valor // 100
    valor %= 100

    notas_50 = valor // 50
    valor %= 50

    notas_20 = valor // 20
    valor %= 20

    notas_10 = valor // 10
    valor %= 10

    notas_5 = valor // 5
    valor %= 5

    notas_2 = valor // 2
    valor %= 2

    if valor != 0:
        print("Erro: valor não pode ser sacado.")
    else:
        print("Notas entregues:")
        if notas_100 > 0:
            print(f"{notas_100} nota(s) de R$100")
        if notas_50 > 0:
            print(f"{notas_50} nota(s) de R$50")
        if notas_20 > 0:
            print(f"{notas_20} nota(s) de R$20")
        if notas_10 > 0:
            print(f"{notas_10} nota(s) de R$10")
        if notas_5 > 0:
            print(f"{notas_5} nota(s) de R$5")
        if notas_2 > 0:
            print(f"{notas_2} nota(s) de R$2")