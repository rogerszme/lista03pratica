
class Pessoa():
    def __init__(self, nome_completo, escolaridade, idade, cpf):
        self.nome_completo = nome_completo
        self.escolaridade = escolaridade
        self.idade = idade
        self.cpf = cpf
    def informacaoSaida(self):
        print(f'Meu Nome é',self.nome_completo.title(),', Escolaridade: ',self.escolaridade.title(),', Tenho',self.idade,'Anos'', CPF:',self.cpf.title(),)

pessoa1 = Pessoa(input('Digite o Nome Completo: '), input('Digite a Escolaridade: '), input('Digite a Idade: '),input('Digite o CPF: '))

pessoa1.informacaoSaida()