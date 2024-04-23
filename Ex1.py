senhaCadastrada = '12432'

for i in range(3):
    senha = input("insira sua senha: ")
    if senha == senhaCadastrada:
        print("acesso liberado")
        break
    print(f"Vc só tem mais {2-i} tentativas")

if senha != senhaCadastrada:
    print('acesso negado')
