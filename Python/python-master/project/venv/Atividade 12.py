print("Bem vindo ao simulador de médias escolares")
n1 = float(input("Digite sua primeira nota e pressione ENTER: "))
n2 = float(input("Digite sua segunda nota e pressione ENTER: "))
freq = float(input("Digite sua porcentagem de faltas (em %) e pressione ENTER: "))
med = (n1+n2)/2
if freq >= 25:
    print("O Aluno está REPROVADO POR FALTA!")
elif med >= 7:
    print("O Aluno está APROVADO!")
elif 5 >= med >= 6.9:
    print("O Aluno está de RECUPERAÇÃO")
else:
    print("O Aluno está REPROVADO, POIS NÃO ATINGIU A MÉDIA")