par = 0
for i in range(10):
    valor = input(f"insira o {i+1}° numero: ")

    while not valor.isnumeric():
        print('insira um numero')
        valor = input(f"insira o {i+1}° m numero: ")

    valor = int(valor)

    if valor % 2 == 0:
        par +=1

print(f'tem numeros {par} pares e {i-par} numero impares ')
