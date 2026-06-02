print("Bem vindo ao validador de Datas!")
dia = int(input("Digite o dia do mês e pressione ENTER: "))
mes= int(input("Digite o mês em formato numérico e pressione ENTER: "))
ano = int(input("Digite o Ano e pressione ENTER: "))
1<= mes <= 12
if dia not in range(1, 31):
    print("Digite um dia válido!")
    exit()
elif mes not in range(1, 12):
    print("Digite um mês válido!")
    exit()
else:
    if mes == 3 or mes == 6 or mes == 9 or mes == 11:
        1<= dia <=30
        print("Mês que possui 30 dias")
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        1<= dia <=31
        print("Mês que possui 31 dias")
    elif mes == 2 and 1 <= dia <= 29 and ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            print("Ano BISSEXTO, com 366 dias")
    else:
        if mes == 2 and 1 <= dia <= 28:
            print("Ano NORMAL, COM 365 DIAS")
        else:
            print("Digite um Ano válido!")

