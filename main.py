from Admin import Admin
from Cliente import Cliente
import os

while True:
    nivel = int(input("1 - Administrador\n2 - Cliente\n3 - Sair\nDigite qm vc é: "))
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