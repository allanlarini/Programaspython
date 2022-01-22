altura = float(input("Informe a altura: "))
sexo = input("Informe o sexo m/f:  ")
if sexo.lower() == 'm':
    peso_ideal = (72.7*altura)-58
elif sexo.lower() == 'f':
    peso_ideal = (62.1*altura)-44.7
else:
    peso_ideal = 0
    print("Sexo nao reconhecido! Favor informar m ou f")
print("O peso ideal eh de {0:.2f} KG.".format(peso_ideal))
