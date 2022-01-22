e = 0
n = int(input("Informe a quantidade de horas: "))
if n > 50:
    e = n-50
    n = n-e
extra = e*20
salario = n*10
print("O salario eh de: R${0}".format(salario))
print("A valor de H.E. eh de: R${0}".format(extra))
