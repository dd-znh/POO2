from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def __init__(self, nome, altura, comprimento, carga, velocidade):
        self.nome = nome
        self.altura = altura
        self.comprimento = comprimento
        self.carga = carga
        self.velocidade = velocidade

class TransporteAereo(Transporte):
    def __init__(self, nome, altura, comprimento, carga, velocidade, autonomia, envergadura):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.autonomia = autonomia
        self.envergadura = envergadura

class TransporteTerrestre(Transporte):
    def __init__(self, nome, altura, comprimento, carga, velocidade, motor, rodas):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.motor = motor
        self.rodas = rodas

class TransporteAquatico(Transporte):
    def __init__(self, nome, altura, comprimento, carga, velocidade, boca, calado):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.boca = boca
        self.calado = calado

class Catalogo:
    def __init__(self):
        self.lista_transporte_aereo = []
        self.lista_transporte_terrestre = []
        self.lista_transporte_aquatico = []
    
    def adicionar_transporte_aereo(self, aereo:TransporteAereo):
        self.lista_transporte_aereo.append(aereo)
    
    def adicionar_transporte_terrestre(self, terrestre:TransporteTerrestre):
        self.lista_transporte_terrestre.append(terrestre)
    
    def adicionar_transporte_aquatico(self, aquatico:TransporteAquatico):
        self.lista_transporte_aquatico.append(aquatico)
    
    def visualizar_catalogo(self):
        for elemento in self.lista_transporte_aereo:
            print(elemento.nome, elemento.altura, elemento.comprimento, elemento.carga, elemento.velocidade, elemento.autonomia, elemento.envergadura)
            print()
        for elemento in self.lista_transporte_terrestre:
            print(elemento.nome, elemento.altura, elemento.comprimento, elemento.carga, elemento.velocidade, elemento.motor, elemento.rodas)
            print()
        for elemento in self.lista_transporte_aquatico:
            print(elemento.nome, elemento.altura, elemento.comprimento, elemento.carga, elemento.velocidade, elemento.boca, elemento.calado)
            print()

c1 = TransporteTerrestre("palio", 1.7, 2.5, 1, 150, "2.0 turbo", 200)
a1 = TransporteAereo("boeing 737", 5, 50, 20, 800, 20000, 25)
cat1 = Catalogo()
cat1.adicionar_transporte_terrestre(c1)
cat1.adicionar_transporte_aereo(a1)
cat1.visualizar_catalogo()