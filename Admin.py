def Admin():
    cadastrar = input("Digite um nome: ")
    
    while True:
        for i in range (1):    
            print("Qual opção desejas realizar: ")
            Opção= int(input)("Se desejas se cadastrar usuário ao banco digite 1\n Para deletar conta de usuário digite 2:  ")

            if Opção== 1:
                nome = input("Digite seu nome e sobrenome: ")
                cpf = input("Digite seu numero de cpf: ")
                chave = input("Digite uma chave de cadastro: ")
                D.update({chave:(nome, cpf) })
                print(f'A conta de {nome} foi criada e ja pode ser utilizada' )
            else:
                chave = input("Digite a chave de usuário que desejas excluir: ")
                print(D.get(chave))
                print( )
                print('Deseja ralmente excuir esta conta\n se sim digite 1\n ')



