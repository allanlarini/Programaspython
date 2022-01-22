vetor1 = []
vetor2 = []
soma = []
for n in range(0, 10):
    valor1 = int(input("Digite um valor para o primeiro vetor: "))
    vetor1.append(valor1)
    valor2 = int(input("Digite um valor para o segundo vetor: "))
    vetor2.append(valor2)
    soma.append(valor1+valor2)
for n in soma:
    print(n)
