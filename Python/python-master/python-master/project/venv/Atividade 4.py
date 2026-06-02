print("Bem vindo ao Decompositor de Segundos!")
segundos_dig = int(input("Digite o tempo em segundos e pressione ENTER: "))
horas_ = segundos_dig // 3600
resto = segundos_dig % 3600
minutos = resto // 60
seg = resto % 60
print(f"{segundos_dig} segundos são: {horas_} horas, {minutos} minutos e {seg} segundos")
