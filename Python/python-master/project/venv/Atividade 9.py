print("Bem vindo a Calculadora Segura")
a = int(input("Digite um número inteiro e pressione ENTER:"))
b = int(input("Digite outro número inteiro e pressione ENTER:"))
operador = input("Digite um operador e ppressione ENTER, Escolha entre(+, -, *, /)")
if operador == "+":
    res = a + b
    print(f"O resultado da soma entre {a} e {b} é: {res}")
elif operador == "-":
    res = a - b
    print(f"O resultado da sbtração entre {a} e {b} é: {res}")
elif operador == "*":
    res = a * b
    print(f"O resultado da multiplicação entre {a} e {b} é: {res}")
elif b == 0 and operador == "/":
    print("Não é possível Dividir por zero")
elif operador == "/":
    res = a / b
    print(f"O resultado da divisão entre {a} e {b} é: {res}")
else:
    print("Escolha uma operação válida Entre (+, -, *, /)")