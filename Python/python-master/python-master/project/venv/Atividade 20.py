print("Bem vindo ao simulador de Pedágio")
print("1. CARRO")
print("2. MOTO")
print("3. ÔNIBUS")
print("4. CAMINHÃO")
pedagio = int(input("Com base na tabela acima, Digite o tipo de veículo e PRESSIONE ENTER: "))
match pedagio:
    case 1:
        res = 12
    case 2:
        res = 6
    case 3:
        res = 24
    case 4:
        eixos = int(input("Digite a quantidade de eixos que o caminhão possui: "))
        if eixos == 1:
            res =  12 * eixos
        else:
            res = 12 * eixos
print(f"TOTAL A PAGAR: R${res}")
