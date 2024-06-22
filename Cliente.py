import getpass
from Admin import Clientes
import os
import random
import string

def Cliente():
    loop = True
    while loop == True:
        usuario = input("Digite o seu usuário: ")

        # Procura se o usuario está cadastrado
        for indice in Clientes:
           
            if Clientes[indice][0] == usuario:
                senha = getpass.getpass("Digite a sua senha: ")
                os.system('cls')

                #Usuário Existe  &&  verificação se a senha está correta
                if Clientes[indice][1] == senha:
                    opcaoCliente(indice)
                    loop = False
                    
                   
        print("usuario não encontrado!")
        if input("Deseja tentar de novo(S/N)? ").upper() == "N":
            break
                
def opcaoCliente(usuario):
    while True:
        while True:
            try:
                os.system('cls')
                print(f"Informações da Conta:\n{Clientes[3]}\n")
                opcao = int(input("Página Cliente\n1 - Depositar\n2 - Sacar\n3 - Ver Saldo\n4 - transferência\n5 - criar um pix\n6 - voltar\nDigite a opção desejada: "))
                os.system('cls')
                break
            except:
                os.system('cls')
                input("Valor Incorreto, pressione ENTER para tentar novamente.")
                
        
        if opcao == 1:
            depositar =  float(input("Digite o valor a ser depositado: "))
            Clientes[usuario][2] = Clientes[usuario][2] + depositar
            os.system('cls')

        if opcao == 2:
            sacar = float(input("Digite o valor a ser sacado: "))
            Clientes[usuario][2] = Clientes[usuario][2] - sacar
            os.system('cls')
        
        elif opcao == 3: 
            print(f"Seu saldo Atual: R${Clientes[usuario][2]:.2f}")
            input("Pressione ENTER para prosseguir...")
            os.system('cls')
        elif opcao == 4:
           
            while True:
                try:
                    destinatario = input("Digite para quem você irá mandar (código PIX): ")
                    if destinatario in codigoExiste():
                        Valor_pix = float(input('Digite o valor que deseja transferir: '))
                    else:
                        print("Código não enconrado!")
                except:
                    if input("Código Inválido! Tentar novamente (S/N): ").upper() == "N":
                        break

            
            
            
        elif opcao == 5:
            pix = gerarcodigo(Clientes)
            print(f"Sua chave pix foi criada!\nChave: {pix}")
            Clientes[usuario].append(pix)
        
        elif opcao == 6:
            break 

def codigoExiste():
    codigo_existente = set()
    for cliente_id in Clientes:
        if len(Clientes[cliente_id]) == 4:  # Verificar se há código para o cliente
            codigo_existente.add(Clientes[cliente_id][3])

def gerarcodigo(Clientes):

    codigosExistentes = codigoExiste()

    while True:
        # Gera um código de 3 letras maiúsculas
        codigo = ''.join(random.choices(string.ascii_uppercase, k=3))
        # Verifica se o código já existe no dicionário
        if codigo not in codigosExistentes:
            return codigo
