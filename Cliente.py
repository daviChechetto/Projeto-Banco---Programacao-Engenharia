import getpass
from Admin import Clientes
import os
import random
import string


def Cliente():
    
    while True:
        usuario = input("Digite o seu usuário: ")
        cont = 0
        # Procura se o usuario está cadastrado
        for indice in Clientes:
            if Clientes[indice][0] == usuario:
                senha = getpass.getpass("Digite a sua senha: ")
                os.system('cls')

                #Usuário Existe  &&  verificação se a senha está correta
                if Clientes[indice][1] == senha:
                    opcaoCliente(indice)
            else:
                cont += 1
        if len(Clientes) == cont:
            print("usuario não encontrado!")
            if input("Deseja tentar de novo(S/N)? ").upper() == "N":
                break
        break
                
def opcaoCliente(usuario):
    while True:
        while True:
            try:
                os.system('cls')
                print(f"Informações da Conta:\n{Clientes[usuario]}\n")
                opcao = int(input("Página Cliente\n1 - Depositar\n2 - Sacar\n3 - Ver Saldo\n4 - Transferência\n5 - Criar um pix\n6 - Voltar\nDigite a opção desejada: "))
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
                    cod_destinatario = input("Digite para quem você irá mandar (código PIX): ")
                    if cod_destinatario in codigoExiste():
                        
                        for cliente_id, cliente_info in (Clientes.items()):
                            if len(cliente_info) > 3 and cliente_info[3] == cod_destinatario:   # Verifica qual é o cliente que tem tal código
                                destinatario = (Clientes[cliente_id])

                        while True:
                            print(f'Você Tem R${Clientes[usuario][2]}')
                            Valor_pix = float(input('Digite o valor que deseja transferir: '))
                            if Valor_pix <= Clientes[usuario][2]:
                                break


                        if input(f"Você irá mandar R${Valor_pix} para o(a) {destinatario[0]}!\nDeseja continuar (S/N)? ").upper() == "S":
                            destinatario[2] += Valor_pix
                            Clientes[usuario][2] -= Valor_pix
                            os.system('cls')
                            print(f"Transferência concluída.")
                            print(f"Seu novo saldo: {Clientes[usuario][2]}")
                            input("Pressione ENTER para prosseguir...")
                        else:
                            print("Transação cancelada!")
                            input("Pressione ENTER para prosseguir...")
                            break
                        break


                    elif input("Código não existe! Tentar novamente (S/N): ").upper() == "N":
                        break
                except Exception as e:
                    input(f"Ocorreu um erro inesperado: {e}\nPressione ENTER para prosseguir...")
                    if input("Código Inválido! Tentar novamente (S/N): ").upper() == "N":
                        break

        elif opcao == 5:
            if len(Clientes[usuario]) < 4:
                pix = gerarCodigo(Clientes)
                print(f"Sua chave pix foi criada!\nChave: {pix}")
                Clientes[usuario].append(pix)
            else:
                print(f"Você já tem uma chave!\nChave: {Clientes[usuario][3]}")
            input("Pressione ENTER para prosseguir...")
        
        elif opcao == 6:
            break 

def codigoExiste():
    codigo_existente = set()
    for cliente_id in Clientes:
        if len(Clientes[cliente_id]) == 4:  # Verificar se há código para o cliente
            codigo_existente.add(Clientes[cliente_id][3])
    return codigo_existente

def gerarCodigo(Clientes):

    codigosExistentes = codigoExiste()

    while True:
        # Gera um código de 3 letras maiúsculas
        codigo = ''.join(random.choices(string.ascii_uppercase, k=3))
        # Verifica se o código já existe no dicionário
        if codigo not in codigosExistentes:
            return codigo
