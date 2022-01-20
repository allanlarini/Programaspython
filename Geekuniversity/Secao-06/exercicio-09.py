poluicao = float(input("Informe o nivel de poluicao: "))
if poluicao >= 0.3 and poluicao < 0.4:
    print("O [Grupo 1] devera suspender as atividades!")
if poluicao >= 0.4 and poluicao < 0.5:
    print("O [Grupo 2] devera suspender as atividades!")
if poluicao >= 0.5:
    print("Todos os Grupos devem suspender suas atividades!")
if poluicao < 0.3:
    print("O nivel de poluicao eh aceitavel.")
