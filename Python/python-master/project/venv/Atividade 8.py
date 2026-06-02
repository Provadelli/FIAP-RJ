print("Bem vindo ao simulador de Imposto de Renda!")
salario_funcionario = float(input("Digite seu Salário bruto em Reais e pressione ENTER: "))
if salario_funcionario <= 2112:
    res = salario_funcionario * 0
    print(f"O Senhor(a) está Insento do imposto de renda, TOTAL A PAGAR R${res:.2f}")
elif 2112.01 <= salario_funcionario <= 2826.65:
    res = salario_funcionario * 0.075
    print(f"O Senhor(a) pagará 7,5% de Imposto de renda, TOTAL A PAGAR R${res:.2f}")
elif 2826.66 <= salario_funcionario <= 3751.05:
    res = salario_funcionario * 0.15
    print(f"O Senhor(a) pagará 15% de Imposto de renda, TOTAL A PAGAR R${res:.2f}")
elif 3751.06 <= salario_funcionario <= 4664.68:
    res = salario_funcionario * 0.225
    print(f"O Senhor(a) pagará 22,5% de Imposto de renda, TOTAL A PAGAR R${res:.2f}")
else:
    res = salario_funcionario * 0.275
    print(f"O Senhor(a) pagará 27,5% de Imposto de renda, TOTAL A PAGAR R${res:.2f}")
