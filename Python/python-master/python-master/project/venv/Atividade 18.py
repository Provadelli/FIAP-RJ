print("Bem vindo ao Conversor de moedas!")
print("Escolha uma opção para a conversão")
print(" 1. Dólar(USD)")
print("2. Euro(EUR)")
print("3. Libra(GBP)")
print("4. Iene(JPY)")
moeda = float(input("Digite o valor EM REAIS, escolha umas das opções acima e PRESSIONE ENTER: "))
convert = int(input("Digite a opçao de conversão desejada, com base na tabela e PRESSIONE ENTER: "))
taxa_cambio = 1.05
match convert:
    case 1:
        res = (moeda / 5.21) * taxa_cambio
    case 2:
        res = (moeda / 6.04) * taxa_cambio
    case 3:
        res = (moeda / 6.97) * taxa_cambio
    case 4:
        res = (moeda / 0.033) * taxa_cambio
    case _:
        print("Digite uma opção VALIDA! (1, 2, 3, 4)")
print(f"O valor convertido é de {res:.2f}")