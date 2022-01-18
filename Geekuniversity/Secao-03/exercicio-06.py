hora_trab = float(input("Informe a quantidade de horas trabalhadas! "))
salario = float(input("Informe o salario/hora! "))
total_mes = (hora_trab*salario)
print("O salario desse mes eh de: R${0:.2f}".format(total_mes))
