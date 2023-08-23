from typing import Any
import math
import random

# 1 a 6:
class Televisao():
    def __init__(self, canal, tamanho, marca, canal_minimo=2, canal_maximo=14): # classe televisao com seus atributos
        self.ligada = False
        self.canal = canal
        self.canal_minimo = canal_minimo
        self.canal_maximo = canal_maximo
        self.tamanho = tamanho
        self.marca = marca
 
    def muda_canal_para_cima(self): # acrescenta 1 no canal exceto quando estiver no ultimo (volta para o primeiro)
        if self.canal < self.canal_maximo:
            self.canal = self.canal + 1
        else:
            self.canal = self.canal_minimo
    
    def muda_canal_para_baixo(self): # decresce 1 no canal exceto quando estiver no primeiro (vai para o ultimo)
        if self.canal > self.canal_minimo:
            self.canal = self.canal - 1
        else:
            self.canal = self.canal_maximo

tv1 = Televisao(7, 55, "Panasonic") # criacao de objetos com seus atributos, utilizacao de metodos, e print dos atributos
tv2 = Televisao(8, 65, "LG")
tv3 = Televisao(6, 40, "LG", canal_minimo=1, canal_maximo=99)
tv2.muda_canal_para_cima()
tv1.muda_canal_para_baixo()
print(tv1.ligada, tv1.canal, tv1.tamanho, tv1.marca)
print(tv2.ligada, tv2.canal, tv2.tamanho, tv2.marca)
print(tv3.ligada, tv3.canal, tv3.tamanho, tv3.marca, tv3.canal_minimo, tv3.canal_maximo)

# 7:

class Estado ():
    def __init__(self, nome, sigla): # classe estado com seus atributos e lista para as cidades pertencentes ao estado
        self.nome = nome
        self.sigla = sigla
        self.cidade = []
        self.populacao = 0
    
    def adicionar_cidade(self, cidade): # metodo para adicionar cidade a lista de cidades do estado
        self.cidade.append(cidade)

    def calcuar_populacao(self): # calcular populacao do estado com base na soma da populacao das cidades pertencentes
        for cidade in self.cidade:
            self.populacao += cidade.populacao

class Cidade (Estado): # classe cidade com seus atributos
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

e1 = Estado("Santa Catarina", "SC") # criacao de objetos, execucao de metodos e print de atributos
e2 = Estado("Rio Grande do Norte", "RN")
e3 = Estado("Rio Grande do Sul", "RS")

c1 = Cidade("Itapema", 80000)
c2 = Cidade("Porto Alegre", 1400000)
c3 = Cidade("Florianopolis", 600000)
c4 = Cidade("Natal", 900000)

e1.adicionar_cidade(c1)
e1.adicionar_cidade(c3)
e3.adicionar_cidade(c2)
e2.adicionar_cidade(c4)

e1.calcuar_populacao()
e2.calcuar_populacao()
e3.calcuar_populacao()

print(e1.populacao, e2.populacao, e3.populacao)

# 8:

class Coordenada(): # classe coordenadas com atributo x e y
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostrar_coordenada(self): # metodo para print da coordenada
        print(self.x, self.y)

    def calcular_distancia(self, obj1): # metodo para calcular distancia entre dois objetos
        print(math.sqrt(((self.x - obj1.x)**2)+((self.y - obj1.y)**2)))
        
    def comparar_coordenadas(self, obj1, obj2): # metodo para comparar duas distancias diferentes
        if math.sqrt(((self.x - obj1.x)**2)+((self.y - obj1.y)**2)) < math.sqrt(((self.x - obj2.x)**2)+((self.y - obj2.y)**2)):
            print("O ponto 1 está mais próximo que o ponto 2")
        elif math.sqrt(((self.x - obj1.x)**2)+((self.y - obj1.y)**2)) == math.sqrt(((self.x - obj2.x)**2)+((self.y - obj2.y)**2)):
            print("A distancia é a mesma")
        else:
            print("O ponto 2 está mais próximo que o ponto 1")
    
    def formato_polar(self): # metodo para printar formato polar da coordenada
        r = math.sqrt((self.x)**2 + (self.y)**2)
        t = math.atan2(self.y, self.x)
        print(r, t)

p1 = Coordenada(2, 3) # criacao de objetos, utilizacao de metodos e print de atributos
p2 = Coordenada(3, 4)
p3 = Coordenada(7, 2)
p4 = Coordenada(0, 0)
p5 = Coordenada(0, 4)
p6 = Coordenada(3, 0)

p1.mostrar_coordenada()
p1.calcular_distancia(p2)
p1.comparar_coordenadas(p2, p3)
p1.formato_polar()

# 9:

class Quadrado(): # classe quadrado com seus atributos
    def __init__(self, lado):
        self.lado = lado

class Retângulo(): # classe retangulo com seus atributos
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
class Círculo(): # classe circulo com seus atributos
    def __init__(self, raio):
        self.raio = raio

# 10:

class Fracao(): # classe fracao com seus atributos
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def soma(self, obj1): # metodo para soma de fracoes
        print((self.numerador * obj1.denominador) + (obj1.numerador * self.denominador), obj1.numerador * self.numerador)
    
    def subtracao(self, obj1): # metodo para subtracao de fracoes
        print((self.numerador * obj1.denominador) - (obj1.numerador * self.denominador), obj1.numerador * self.numerador)
    
    def multiplicacao(self, obj1): # metodo para multiplicacao de fracoes
        print(self.numerador * obj1.numerador, self.denominador * obj1.denominador)

    def divisao(self, obj1): # metodo para divisao de fracoes
        print(self.numerador * obj1.denominador, self.denominador * obj1.numerador)
    