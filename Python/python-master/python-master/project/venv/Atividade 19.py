print("Bem vindo ao classificador de meses e dias!")
mes = int(input("Digite um número de 1 a 12 e PRESSIONE ENTER: "))
match mes:
    case 4 | 6 | 9 | 11:
        print("Mês que possui 30 dias!")
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("Mês que possui 31 dias!")
    case 2:
        print("Fevereiro, podendo ter 28 ou 29 dias (Ano bissexto)!")
    case _:
        print("Digite um mês VÁLIDO!")