# Projeto Banco em Python

Este projeto foi desenvolvido como parte da disciplina de Programação para Engenharia. Ele simula um sistema bancário simples, permitindo operações básicas como cadastro de clientes, login, depósitos, saques, transferências e criação de chaves PIX.

## Sumário

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Executar](#como-executar)
- [Exemplo de Uso](#exemplo-de-uso)
- [Autor](#autor)

## Visão Geral

O sistema bancário simula as funcionalidades básicas de um banco, incluindo a administração de contas de clientes e a realização de operações financeiras. Ele possui dois níveis de acesso: administrador e cliente.

## Funcionalidades

### Administrador

- **Cadastrar Usuário:** Permite o cadastro de novos clientes.
- **Deletar Usuário:** Remove clientes existentes.
- **Mostrar Todos os Usuários:** Lista todos os clientes cadastrados.

### Cliente

- **Depositar:** Permite que o cliente deposite dinheiro em sua conta.
- **Sacar:** Permite que o cliente saque dinheiro de sua conta.
- **Ver Saldo:** Exibe o saldo atual da conta do cliente.
- **Transferência:** Permite a transferência de dinheiro para outra conta utilizando uma chave PIX.
- **Criar um PIX:** Gera uma nova chave PIX para o cliente.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

```plaintext
├── Admin.py
├── Cliente.py
├── main.py
└── README.md
```
## Como Executar

1. **Clone o repositório:**
```
git clone https://github.com/seu-usuario/seu-repositorio.git
```
2. **Navegue até o diretório do projeto:**

```
cd seu-repositorio
```
3. **Execute o programa principal:**

```
python main.py
```

## Exemplo de Uso
Ao iniciar o programa, você verá um menu inicial que permite escolher entre Administrador, Cliente ou Sair do Programa. Dependendo da escolha, você será levado para os respectivos menus e poderá realizar as operações disponíveis.

### Administrador
Cadastro de Cliente: Insira o nome e a senha do novo cliente.
Deleção de Cliente: Insira o ID do cliente a ser removido.
Listar Clientes: Exibe todos os clientes cadastrados.

### Cliente
Depósito: Insira o valor a ser depositado.
Saque: Insira o valor a ser sacado.
Ver Saldo: Exibe o saldo atual.
Transferência: Insira a chave PIX do destinatário e o valor a ser transferido.
Criar PIX: Gera uma nova chave PIX única.

## Autor
Este projeto foi desenvolvido por Davi Chechetto, junto a Gabriel Tramontin e Nicola Antunes, como parte da disciplina de Programação para Engenharia.
