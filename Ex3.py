soma = 0
for i in range(10):
    valor = input(f"insira o {i+1}° numero: ")

    while not valor.isnumeric():
        print('INSIRA UM NUMERO')
        valor = input(f"insira o {i+1}° numero: ")

    valor = int(valor)
    soma += valor

print(f"a soma dos numero inseridos é: {soma} e a sua média é {soma/i}")
