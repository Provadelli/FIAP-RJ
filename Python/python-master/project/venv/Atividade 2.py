print("Bem vindo ao Conversor de Temperaturas Inteligente")
temp_atual = float(input("Digite a temperatura atual e pressione ENTER: "))
print("Escolha (C) para Celsius e (F) para Fahrenheit")
escala_ = input("Digite a escala atual da temperatura conforme as opções acima e pressione ENTER: ").upper()
if escala_ == "C":
    fahrennheit =  temp_atual * 1.8 + 32
    print(f"A Temperatura em Fahrenheit: {fahrennheit:.2f}ºF")
elif escala_ == "F":
    celcius = 1.8 * (temp_atual - 32)
    print(f"A Temperatura em Celcius: {celcius:.2f}ºC")
else:
    print("Escala Invalida! Digite 'C' ou 'F'. ")