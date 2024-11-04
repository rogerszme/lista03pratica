class ContaBancaria:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 1000
        print('#################################################')
        print(f'Saldo anterior é: R$:{self.saldo:.2f}')
        print('#################################################')
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print('#################################################')
            print(f'Depósitado o valor de R$ {valor:.2f} com sucesso! ')
        else:
            print('Valor do DEPÓSITO deve ser positivo.')
    def imprimir_saldo(self):
        print('#################################################')
        print(f'Cliente: {self.nome.title()}')
        print(f'Saldo atual: R$:{self.saldo:.2f}')
        print('#################################################')

conta = ContaBancaria((input('Digite o Nome do CLIENTE: ')))
conta.depositar (int(input('Digite o Valor do DEPÓSITO: ')))
conta.imprimir_saldo()