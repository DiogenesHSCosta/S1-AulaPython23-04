par = 0
for i in range(1, 11):
    valor = input(f"insira o {i}° numero: ")

    while not valor.isnumeric():
        print('insira um numero')
        valor = input(f"insira o {i}° m numero: ")

    valor = int(valor)

    if valor % 2 == 0:
        par +=1

print(par)
print(f'tem numeros {par} pares e {i-par} numero impares ')
