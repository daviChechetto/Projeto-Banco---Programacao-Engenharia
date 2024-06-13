import getpass

def Cliente():
    usuario = input("Digite o seu usuário: ")
    senha = getpass.getpass("Digite a sua senha: ")

    opcao = int(input("1 - Depositar\n2 - Sacar\n3 - Voltar\nDigite qm vc é: "))

    depositar =  float(input("Digite um nome: "))

