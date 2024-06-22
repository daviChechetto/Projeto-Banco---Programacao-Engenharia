import os
import getpass

    #ID : [usuario, senha, saldo, chave-pix]
Clientes = {
    1 : ["Gabriel", "senha", 0, "XXX"],
    2 : ["Valentina", "senha123", 0, "YYY"],
    3 : ["a", "a", 0],
}

    #ID : [usuario, senha] 
Admins = { 0 : ["admin", "admin"]}

def Admin():
    
    while True:
        usuario = input("Digite o seu usuário: ")

        # Procura se o usuario está cadastrado
        for i in Admins:
           
            if Admins[i][0] == usuario:
                senha = getpass.getpass("Digite a sua senha: ")
                os.system('cls')

                #Usuário Existe  &&  verificação se a senha está correta
                if Admins[i][1] == senha:
                    opcaoAdmin()
                    break

                   
        print("usuario não encontrado!")
        if input("Deseja tentar de novo(S/N)? ").upper() == "N":
            break

def opcaoAdmin():
    while True:
        while True:
            try:
                os.system('cls')
                opcao= int(input("Página ADMIN\n1 - Cadastrar Usuario\n2 - Deletar Usuario\n3 - Mostrar Todos os Usuários\n4 - Voltar\nQual opção desejas realizar: "))
                os.system('cls')
                break
            except:
                os.system('cls')
                print("Valor Incorreto, tente novamente.")

        if opcao == 1:
            nome = input("Digite o nome do cliente: ")
            senha = input("Digite uma nova senha para o cliente: ")
            
            ncodigo = 1
            
            for i, va in Clientes.items():
                if i != ncodigo:
                    break
                else:
                    ncodigo += 1
        
            Clientes[ncodigo] = [nome, senha, 0]

            """ os.system('cls') """
            print(f'A conta de {nome} foi criada e ja pode ser utilizada' )
            input("Pressione ENTER para prosseguir...")
            os.system('cls')

        elif opcao == 2:
            idDelete = int(input("Digite o ID do usuário que desejas excluir: "))
            try:
                input(f"Usuário '{Clientes[idDelete][0]}' deletado com sucesso.\nPressione ENTER para prosseguir...")
                del Clientes[idDelete]
            except KeyError:
                input("ID não encontrado\nPressione ENTER para prosseguir...")
            except Exception as e:
                input(f"Ocorreu um erro inesperado: {e}\nPressione ENTER para prosseguir...")
            finally: 
                os.system('cls')

        elif opcao == 3:
            print("Usuários:\nID  -  Nome")
            for key, value in sorted(Clientes.items()): 
                print(f"{key} - {value[0]}")
            input("\nPressione ENTER para prosseguir...")
            os.system('cls')

        else:
            print("Você saiu do Admin")
            break
