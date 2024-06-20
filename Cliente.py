import getpass
from Admin import D
import os

def Cliente():
    
    while True:
        usuario = input("Digite o seu usuário: ")
        os.system('cls')

        # Procura se o usuario está cadastrado
        for i in D:
           
            if D[i][0] == usuario:
                print("usuario encontrado!")
                senha = getpass.getpass("Digite a sua senha: ")
                os.system('cls')

                #Usuário Existe  &&  verificação se a senha está correta
                if D[i][1] == senha:
                    print("senha correta!")
                    opecaoCliente(i)
                    break

                   
        print("usuario não encontrado!")
                
def opecaoCliente(i):
    while True:
        opcao = int(input("1 - Depositar\n2 - Sacar\n3 - Ver Saldo\n4 - transferência\n5 - criar um pix\n6 - voltar\nDigite a opção desejada: "))
        os.system('cls')
        
        if opcao == 1:
            depositar =  float(input("Digite o valor a ser depositado: "))
            D[i][2] = D[i][2] + depositar
            os.system('cls')

        if opcao == 2:
            sacar = float(input("Digite o valor a ser sacado: "))
            D[i][2] = D[i][2] - sacar
            os.system('cls')
        
        elif opcao == 3: 
            print(f"Seu saldo Atual: {D[i][2]}")
            input("Pressione ENTER para prosseguir...")
            os.system('cls')
        elif opcao == 4:
            Valor_pix = int(input('Digite o número do pix que deseja fazer a transferência'))
            
            
            
            

        
        
        elif opcao == 5:
            pix = float('Fum valor para o pix')
            D[i][4] = pix
        
        elif opcao == 6:
            break 