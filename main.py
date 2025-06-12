class Veiculo:
    def __init__(self, modelo, ano, cor, quilometragem):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem

    def exibir_detalhes(self):
        return (
            f"Modelo: {self.modelo}\n"
            f"Ano: {self.ano}\n"
            f"Cor: {self.cor}\n"
            f"Quilometragem: {self.quilometragem} km"
        )

    def calcular_valor_revenda(self, valor_base, fator_depreciacao):
        return f'Valor de revenda: {valor_base - (self.quilometragem * fator_depreciacao)}'

    def tipo_veiculo(self, tipo):
        return f'Tipo: {tipo}'


class Carro(Veiculo):
    def __init__(self, modelo, ano, cor, quilometragem, num_portas):
        super().__init__(modelo, ano, cor, quilometragem)
        self.num_portas = num_portas

    def tipo_veiculo(self):
        return super().tipo_veiculo('Carro')

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return f"=== Detalhes do Veículo ===\nTipo: {self.tipo_veiculo()}\n{detalhes}\nNúmero de portas: {self.num_portas}"

    def calcular_valor_revenda(self, valor_base, fator_depreciacao):
        return super().calcular_valor_revenda(valor_base, fator_depreciacao)


class Moto(Veiculo):
    def __init__(self, modelo, ano, cor, quilometragem, cilindrada):
        super().__init__(modelo, ano, cor, quilometragem)
        self.cilindrada = cilindrada

    def tipo_veiculo(self):
        return super().tipo_veiculo('Moto')

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return f"=== Detalhes do Veículo ===\nTipo: {self.tipo_veiculo()}\n{detalhes}\nCilindrada: {self.cilindrada}cc"
    
    def calcular_valor_revenda(self, valor_base, fator_depreciacao):
        return super().calcular_valor_revenda(valor_base, fator_depreciacao)


class Barco(Veiculo):
    def __init__(self, modelo, ano, cor, quilometragem, tipo_propulsao):
        super().__init__(modelo, ano, cor, quilometragem)
        self.tipo_propulsao = tipo_propulsao

    def tipo_veiculo(self):
        return super().tipo_veiculo('Barco')

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return f"=== Detalhes do Veículo ===\nTipo: {self.tipo_veiculo()}\n{detalhes}\nTipo de propulsão: {self.tipo_propulsao}"
    
    def calcular_valor_revenda(self, valor_base, fator_depreciacao):
        return super().calcular_valor_revenda(valor_base, fator_depreciacao)


class Aviao(Veiculo):
    def __init__(self, modelo, ano, cor, quilometragem, tipo_combustivel):
        super().__init__(modelo, ano, cor, quilometragem)
        self.tipo_combustivel = tipo_combustivel

    def tipo_veiculo(self):
        return super().tipo_veiculo('Avião')

    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return f"=== Detalhes do Veículo ===\nTipo: {self.tipo_veiculo()}\n{detalhes}\nTipo de combustível: {self.tipo_combustivel}"

    def calcular_valor_revenda(self, valor_base, fator_depreciacao):
        return super().calcular_valor_revenda(valor_base, fator_depreciacao)


"""
POLIMORFISMO

def mostrar_informacoes(veiculos):
    for veiculo in veiculos:
        print(veiculo.exibir_detalhes())
        print(f"Valor de revenda: R$ {veiculo.calcular_valor_revenda():.2f}")
        print("-" * 26)

veiculos = [
    Carro("Toyota Corolla", 2020, "Branco", 45000, 4),
    Moto("Honda CB 500", 2019, "Branco", 15000, 500),
    Barco("Lancha 3000", 2015, "Branco", 200, "Motor de popa"),
    Aviao("Boeing 737", 2010, "Branco", 80000, "Querosene")
]

mostrar_informacoes(veiculos)
"""

carro = Carro('Toyota Corolla', 2020, "Branco", 45000, 4)
print(carro.exibir_detalhes())
print(carro.calcular_valor_revenda(47500, 2))

moto = Moto('Honda CB 500', 2019, 'Branco', 15000, 500)
print(moto.exibir_detalhes())
print(moto.calcular_valor_revenda(11600, 0.5))

barco = Barco('Lancha 3000', 2015, 'Branco', 200, "Motor de popa")
print(barco.exibir_detalhes())
print(barco.calcular_valor_revenda(110000, 1.25))

aviao = Aviao('Boeing 737', 2010, 'Branco', 80000, "Querosene")
print(aviao.exibir_detalhes())
print(aviao.calcular_valor_revenda(400000, 1.5))