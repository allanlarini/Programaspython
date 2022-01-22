n1 = int(input("Insira o primeiro numero: "))
n2 = int(input("Insira o segundo numero: "))
n3 = int(input("Insira o terceiro numero: "))
n4 = int(input("Insira o quarto numero: "))
q1 = n1**2
q2 = n2**2
q3 = n3**2
q4 = n4**2
if q3 >= 1000:
    print("O valor do quadrado de {0} eh = {1}".format(n3, q3))
else:
    print("O valor do quadrado de {0} eh = {1}".format(n1, q1))
    print("O valor do quadrado de {0} eh = {1}".format(n2, q2))
    print("O valor do quadrado de {0} eh = {1}".format(n3, q3))
    print("O valor do quadrado de {0} eh = {1}".format(n4, q4))
