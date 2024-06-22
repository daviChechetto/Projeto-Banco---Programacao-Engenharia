from Admin import Admin
from Cliente import Cliente
import os

while True:
    while True:
        try:
            os.system('cls')
            nivel = int(input("Página Inicial\n1 - Administrador\n2 - Cliente\n3 - Sair do Programa\nDigite o seu nível de usuário: "))
            os.system('cls')
            break
        except:
            os.system('cls')
            print("Valor Incorreto, tente novamente.")

    if nivel == 1:
        Admin()
    elif nivel == 2:
        Cliente()
    elif nivel == 3:
        print("Saiu!")
        break
    else:
        print("Erro, operador inválido!") 
    
print("Fim do programa!")