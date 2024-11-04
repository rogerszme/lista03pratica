class Carro:
    def __init__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor
    def caracteristicas(self):
        return f"Marca: {self.marca}, Ano: {self.ano}, Cor: {self.cor}"

carro1 = Carro("Corolla", 2024, "Azul")
carro2 = Carro("Civic", 2022, "Preto")
carro3 = Carro("Mustang", 2024, "Marron")
carro4 = Carro("HB20s", 2022, "Prata")
carro5 = Carro("Gol", 2023, "Branco")
carro6 = Carro("Ferrari", 1990, "Vermelho")

veiculos = [carro1, carro2, carro3, carro4, carro5, carro6]
for veiculo in veiculos:
    print(veiculo.caracteristicas())