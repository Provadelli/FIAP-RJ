print("Bem vindo ao Pedra, Papel e Tesoura!")
jogador_1 = input("JOGADOR 1: Escolha entre PEDRA, PAPEL e TESOURA, E PRESSIONE ENTER para jogar: ").upper()
jogador_2 = input("JOGADOR 2: Escolha entre PEDRA, PAPEL e TESOURA, E PRESSIONE ENTER para jogar: ").upper()
if jogador_1 == jogador_2:
    print("EMPATE!")
elif jogador_1 == "PEDRA":
    if jogador_2 == "TESOURA":
        print("JOGADOR 1 VENCEU!")
    else:
        print("JOGADOR 2 VENCEU!")
elif jogador_1 == "PAPEL":
    if jogador_2 == "PEDRA":
        print("JOGADOR 1 VENCEU!")
    else:
        print("JOGADOR 2 VENCEU!")
elif jogador_1 == "TESOURA":
    if jogador_2 == "PAPEL":
        print("JOGADOR 1 VENCEU!")
    else:
        print("JOGADOR 2 VENCEU!")
else:
    print("DIGITE UMA OPÇÃO VÁLIDA!")