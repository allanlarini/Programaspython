hora_trab = float(input("Informe a quantidade de horas trabalhadas! "))
salario = float(input("Informe o salario/hora! "))
total_mes = round((hora_trab*salario), 2)
print("O salario desse mes eh de: R${0}".format(total_mes))
