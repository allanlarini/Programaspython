vetor = []
codigo = int(input("Digite o codigo: "))
if codigo != 0:
    for n in range(0, 5):
        valor = float(input("Insira um valor({0}/5): ".format(n+1)))
        vetor.append(valor)
    if codigo == 1:
        print(vetor)
    if codigo == 2:
        vetor.reverse()
        print(vetor)
