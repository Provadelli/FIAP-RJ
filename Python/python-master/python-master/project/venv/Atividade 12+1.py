import math
print("Bem vindo ao identificador de raízes da equação do segundo grau")
a = int(input("Digite o valor da variável (A) da equação e pressione ENTER:"))
b = int(input("Digite o valor da variável (B) da equação e pressione ENTER:"))
c = int(input("Digite o valor da variável (C) da equação e pressione ENTER:"))
if a == 0:
    print("Não é uma equação do segundo grau")
    exit()
delta = b ** 2 - 4 * a * c
print(f"Delta calculado: {delta}")
if delta < 0:
        print("Não há RAIZES REAIS, pois DELTA é NEGATIVO!")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print(f"A equação possui uma ÚNICA RAIZ REAL: {x1:.2f}")
    else:
        print(f"As raízes são: x1 = {x1:.2f}, x2 = {x2:.2f}")

