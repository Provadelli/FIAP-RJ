print("Bem vindo a calculadora de IMC")
nome_usuario = input("Digite Seu Nome e pressione ENTER: ")
peso_usuario = float(input("Digite Seu Peso em quilogramas e pressione ENTER: "))
altura_usuario = float(input("Digite Sua Altura em metros e pressione ENTER: "))
imc = peso_usuario / (altura_usuario ** 2)
if imc < 18.5:
    resultado = ("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    resultado = ("Peso normal")
elif 25 <= imc < 29.9:
    resultado = ("Sobrepeso")
elif 30 <= imc < 34.9:
    resultado = ("Obesidade grau 1")
elif 35 <= imc < 39.9:
    resultado = ("Obesidade grau 2")
else:
    resultado = ("Obesidade grau 3 (Mórbida ")
print(f"O usuário {nome_usuario} está com {resultado} e o IMC no valor de {imc:.2f}")