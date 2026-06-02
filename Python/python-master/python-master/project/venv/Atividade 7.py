print("Bem vindo ao simulador de Aposentadoria!")
idade_ = int(input("Digite sua idade e pressione ENTER:"))
tempo_de_trabalho= int(input("Digite o tempo de contribuição em anos e pressione ENTER:"))
if idade_ >= 65 or tempo_de_trabalho >= 30 or idade_ >= 60 and tempo_de_trabalho >= 25:
    print(f"O senhor(a) PODE SE APOSENTAR! Pois tem {idade_} anos e {tempo_de_trabalho} anos de trabalho")
else:
    print("O Senhor(a) NÃO PODE SE APOSENTAR! Pois não atende aos requisitos")