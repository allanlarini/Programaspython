qtd_mouse = 0
def_1 = 0
def_2 = 0
def_3 = 0
def_4 = 0
id = int(input("Informe o numero de ID:"))
while id != 0:
    print("1-Necessita da esfera.")
    print("2-Necessita de limpeza.")
    print("3-Necessita troca do cabo ou conector.")
    print("4-Quebrado ou inutilizado.")
    defeito = int(input("Informe o codigo de defeito conforme tabela acima: "))
    if defeito == 1:
        def_1 = def_1+1
    elif defeito == 2:
        def_2 = def_2+1
    elif defeito == 3:
        def_3 = def_3+1
    elif defeito == 4:
        def_4 = def_4+1
    qtd_mouse = qtd_mouse+1
    id = int(input("Informe o numero de ID:"))
per_1 = (def_1*100)/qtd_mouse
per_2 = (def_2*100)/qtd_mouse
per_3 = (def_3*100)/qtd_mouse
per_4 = (def_4*100)/qtd_mouse
print("Situacao                             Quantidade          Percentual")
print(
    "1-Necessita da esfera                   {0}                 {1:.2f}".format(def_1, per_1))
print(
    "2-Necessita de limpeza                  {0}                 {1:.2f}".format(def_2, per_2))
print(
    "3-Necessita troca do cabo/conect.       {0}                 {1:.2f}".format(def_3, per_3))
print(
    "4-Quebrado ou inutilizado               {0}                 {1:.2f}".format(def_4, per_4))
