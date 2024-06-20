import getpass
from Admin import D

def Cliente():
    
    while True:
        usuario = input("Digite o seu usuário: ")
        senha = getpass.getpass("Digite a sua senha: ")

        # Procura se o usuario está cadastrado
        for i in D:
           
            if D[i][0] == usuario:
                print("usuario encontrado!")

                #Usuário Existe  &&  verificação se a senha está correta
                if D[i][1] == senha:
                    print("senha correta!")
            
                    opcao = int(input("1 - Depositar\n2 - Sacar\n3 - Voltar\nDigite a opção desejada: "))

                    if opcao == 1:
                        depositar =  float(input("Digite um nome: "))
        
        print("usuario não encontrado!")

