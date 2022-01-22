vetor = []
soma = 0
for num in range(0, 20):
    valor = int(input("Digite um valor ({0}/20): ".format(num+1)))
    vetor.append(valor)
    soma = (soma+valor)
print("O total da soma dos valores eh de: {0}".format(soma))
