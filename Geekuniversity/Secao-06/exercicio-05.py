e = 0
m = 0
peso = int(input("Informe o peso do peixe: "))
if peso > 50:
    e = peso-50
    m = e*4
else:
    print("O peso esta abaixo de 50KG.")
print("O peso do peixe eh: {0:.2f}".format(peso))
print("O excesso eh de: {0:.2f}".format(e))
print("O valor da multa a pagar eh de: {0:.2f}".format(m))
