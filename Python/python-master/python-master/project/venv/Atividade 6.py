print("Bem vindo ao identificador de triangulos")
lado1 = int(input("Digite o valor do primeiro lado do triângulo e pressione ENTER: "))
lado2 = int(input("Digite o valor do segundo lado do triângulo e pressione ENTER: "))
lado3 = int(input("Digite o valor do terceiro lado do triângulo e pressione ENTER: "))
if (lado1 + lado2) <= lado3 or (lado1 + lado3) <= lado2 or (lado2 + lado3) <= lado1:
    print("Triângulo Inválido!")
    exit()
else:
    print("Triângulo Valido!")
if lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
    print("Triângulo Isósceles, Pois possui dois lados iguais e um diferente")
elif lado1 == lado2 == lado3:
    print("Triângulo Equilátero, Pois possui todos os lados iguais")
else:
    print("Triângulo Escaleno, Pois possui todos os lados diferentes")

