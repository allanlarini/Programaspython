num = int(input("Informe o numero da tabuada de 1 a 10: "))
while num < 1 or num > 10:
    num = int(input("Informe o numero da tabuada de 1 a 10: "))
print("A tabuada de {0} eh: ".format(num))
for n in range(1, 11):
    print("{0} X {1} = {2}".format(num, n, (num*n)))
