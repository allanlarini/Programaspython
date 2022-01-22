vetor = []
maior_50 = False
for n in range(0, 10):
    valor = int(input("Digite um valor({0}/10): ".format(n+1)))
    vetor.append(valor)
for n in vetor:
    if n > 50:
        print("O valor {0} na posicao {1} eh maior que 50".format(
            n, vetor.index(n)))
        maior_50 = True
if maior_50 is False:
    print("Nao ha valores maior que 50!")
