class Veiculo:
    def __init__(self, modelo, ano, cor, quilometragem):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem

    def exibir_detalhes(self):
        print(f'Modelo: {self.modelo}')
        print(f'Ano: {self.ano}')
        print(f'Cor: {self.cor}')
        print(f'Quilometragem: {self.quilometragem} km')

    def tipo_veiculo(self, tipo):
        print(f'Tipo: {tipo}')

    def calcular_valor_revenda(self, valor_base, fator_depreciacao):
        return valor_base - (self.quilometragem * fator_depreciacao)


class Carro(Veiculo):
    def __init__(self, modelo, ano, cor, quilometragem, num_portas):
        super().__init__(modelo, ano, cor, quilometragem)
        self.num_portas = num_portas

    def exibir_detalhes(self):
        print(f'Número de portas: {self.num_portas}')
        return super().exibir_detalhes()

    def tipo_veiculo(self):
        return super().tipo_veiculo('Carro')


class Moto(Veiculo):
    def __init__(self, modelo, ano, cor, quilometragem, cilindrada):
        super().__init__(modelo, ano, cor, quilometragem)
        self.cilindrada = cilindrada

    def tipo_veiculo(self, tipo):
        return super().tipo_veiculo('Moto')


class Barco(Veiculo):
    def __init__(self, modelo, ano, cor, quilometragem):
        super().__init__(modelo, ano, cor, quilometragem)
    
    def tipo_veiculo(self, tipo):
        return super().tipo_veiculo('Barco')


class Aviao(Veiculo):
    def __init__(self, modelo, ano, cor, quilometragem, combustivel_aviao):
        super().__init__(modelo, ano, cor, quilometragem)
        self.combustivel_aviao = combustivel_aviao

    def tipo_veiculo(self, tipo):
        return super().tipo_veiculo('Avião')

carro = Carro('Teste', 2020, 'Branco', 10000, 4)
carro.exibir_detalhes()
carro.tipo_veiculo()