print("Bem vindo ao identificador de Ano bissexto")
ano_dig = int(input("Digite o Ano que deseja verificar e pressione ENTER: "))
if ano_dig % 4 == 0 and ano_dig % 100 != 0 or ano_dig % 400 == 0:
    print(f"O Ano {ano_dig} é Bissexto, portanto, tem 366 dias")
else:
    print(f"o Ano {ano_dig} não é bissexto, portanto, tem 365 dias")