print("Bem vindo ao simulador de quadrantes em um ponto cartesiano")
a = int(input("Digite a coordenada do eixo X e pressione ENTER:"))
b = int(input("Digite a coordenada do eixo Y e pressione ENTER:"))
if a > 0 and b > 0:
    print("As coordenadas Escolhidas se encontram no PRIMEIRO QUADRANTE (Q1)")
elif a < 0 and b > 0:
    print("As coordenadas Escolhidas se encontram no SEGUNDO QUADRANTE (Q2)")
elif a < 0 and b < 0:
    print("As coordenadas Escolhidas se encontram no TERCEIRO QUADRANTE (Q3)")
elif a > 0 and b < 0:
    print("As coordenadas Escolhidas se encontram no QUARTO QUADRANTE (Q4)")
else:
    print("As coordenadas Escolhidas se encontram na ORIGEM (PONTO 0,0 )")