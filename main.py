from Admin import Admin
from Cliente import Cliente

while True:
    nivel = int(input("1 - Administrador\n2 - Cliente\n3 - Sair\nDigite qm vc é: "))
    if nivel == 1:
        Admin()
        break
    elif nivel == 2:
        Cliente()
        break
    elif nivel == 3:
        print("Saiu!")
        break
    else:
        print("Erro, operador inválido!")
    



    
























""" for i in range(1):
    nome = input("Digite seu nome e sobrenome: ")
    cpf = input("Digite seu numero de cpf: ")
    chave = input("Digite uma chave de cadastro: ")
    D.update({(nome , cpf):chave})
print(f'Agradecemos pela confiança {nome}, sua conta já foi criada e está pronta para uso.' ) """
