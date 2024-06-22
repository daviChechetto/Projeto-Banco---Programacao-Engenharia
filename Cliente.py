import getpass
from Admin import Clientes
import os

def Cliente():
    
    while True:
        usuario = input("Digite o seu usuário: ")
        os.system('cls')

        # Procura se o usuario está cadastrado
        for indice in Clientes:
           
            if Clientes[indice][0] == usuario:
                print("usuario encontrado!")
                senha = getpass.getpass("Digite a sua senha: ")
                os.system('cls')

                #Usuário Existe  &&  verificação se a senha está correta
                if Clientes[indice][1] == senha:
                    print("senha correta!")
                    opcaoCliente(indice)
                    break

                   
        print("usuario não encontrado!")
        if input("Deseja tentar de novo(S/N)? ").upper() == "N":
            break
                
def opcaoCliente(usuario):
    while True:
        while True:
            try:
                os.system('cls')
                opcao = int(input("Página Cliente\n1 - Depositar\n2 - Sacar\n3 - Ver Saldo\n4 - transferência\n5 - criar um pix\n6 - voltar\nDigite a opção desejada: "))
                os.system('cls')
                break
            except:
                os.system('cls')
                print("Valor Incorreto, tente novamente.")
        
        if opcao == 1:
            depositar =  float(input("Digite o valor a ser depositado: "))
            Clientes[usuario][2] = Clientes[usuario][2] + depositar
            os.system('cls')

        if opcao == 2:
            sacar = float(input("Digite o valor a ser sacado: "))
            Clientes[usuario][2] = Clientes[usuario][2] - sacar
            os.system('cls')
        
        elif opcao == 3: 
            print(f"Seu saldo Atual: {Clientes[usuario][2]}")
            input("Pressione ENTER para prosseguir...")
            os.system('cls')
        elif opcao == 4:
            Valor_pix = int(input('Digite o número do pix que deseja fazer a transferência'))
            
            
        elif opcao == 5:
            pix = float('Fum valor para o pix')
            Clientes[usuario][4] = pix
        
        elif opcao == 6:
            break 