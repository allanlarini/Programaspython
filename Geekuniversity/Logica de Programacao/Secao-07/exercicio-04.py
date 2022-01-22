maior = -999
menor = 999
soma = 0
for n in range(1, 11):
    valor = int(input("Informe um valor: "))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    soma = soma+valor
else:
    valor = int(input("Informe um valor: "))
media = soma/10
print("O maior numero eh: {0}".format(maior))
print("O menor numero eh: {0}".format(menor))
print("A soma dos numeros eh de {0}".format(soma))
print("A media dos valores eh de {0}".format(media))
