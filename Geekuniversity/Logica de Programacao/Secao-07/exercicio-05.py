nome = input("Informe o nome.")
senha = input("Informe a senha.")
while senha == nome:
    print("A senha nao pode ser igual o nome!")
    nome = input("Informe o nome.")
    senha = input("Informe a senha.")
if senha != nome:
    print("Ok. Acesso garantido.")
