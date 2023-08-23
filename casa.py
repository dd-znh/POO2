class Terreno():
    def __init__(self, tam_grama, portao_aberto:bool, comprimento, largura):
        self.tam_grama = tam_grama
        self.portao_aberto = portao_aberto
        self.comprimento = comprimento
        self.largura = largura
    
    def cortar_grama(self):
        self.tam_grama = 5
    
    def estado_portao(self):
        self.portao_aberto = not self.portao_aberto

t1 = Terreno(10, False, 100, 100)
t2 = Terreno(15, True, 50, 50)

t1.cortar_grama()
t2.estado_portao()

print(t1.tam_grama, t1.portao_aberto)
print(t2.tam_grama, t2.portao_aberto)