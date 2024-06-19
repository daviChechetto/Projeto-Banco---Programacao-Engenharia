D = {"id" : ["usuario", "senha", "saldo"]}

def Admin():
    
    while True:
    
        opcao= int(input("1 - Cadastrar Usuario\n2 - Deletar Usuario\nQual opção desejas realizar: "))

        if opcao == 1:
            nome = input("Digite o nome do cliente ")
            senha = input("Digite uma nova senha para o cliente: ")

            D[id] = [nome, senha, 0]

            print(f'A conta de {nome} foi criada e ja pode ser utilizada' )
        elif opcao == 2:
            chave = input("Digite a chave de usuário que desejas excluir: ")
            print(D.get(chave))
            print( )
            print('Deseja ralmente excuir esta conta\n se sim digite 1\n ')
        else:
            print("Você saiu do Admin")
            break



