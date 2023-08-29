class Tabuleiro:
    def __init__(self):
        self.tabuleiro_jog1 = {}
        self.tabuleiro_jog2 = {}
        for i in range(10):
            for j in range(10):
                self.tabuleiro_jog1[(i, j)] = False
                self.tabuleiro_jog2[(i, j)] = False

    def adicionar_barco(self, jogador, coordenadas):
        self.coordenadas = coordenadas
        self.jogador1 = jogador
        if self.jogador1:
            self.tabuleiro_jog1[coordenadas] = True
        else:
            self.tabuleiro_jog2[coordenadas] = True
        print("barco adicionado com sucesso")

    def atacar(self, jogador, coordenada):
        self.coordenada = coordenada
        self.jogador1 = jogador
        if self.jogador1:
            if self.tabuleiro_jog1[coordenada] == True:
                print("voce atacou um navio inimigo")
                self.tabuleiro_jog1[coordenada] = False
                self.resultado()
        else:
            if self.tabuleiro_jog2[coordenada] == True:
                print("voce atacou um navio inimigo")
                self.tabuleiro_jog2[coordenada] = False
                self.resultado()    

    def resultado(self):
        jogador1ganhou = True
        jogador2ganhou = True
        for i in range(10):
            for j in range(10):
                if self.tabuleiro_jog1[(i, j)] == True:
                    jogador2ganhou = False
                if self.tabuleiro_jog2[(i, j)] == True:
                    jogador1ganhou = False
        if jogador1ganhou and not jogador2ganhou:
            print("jogador 1 ganhou")
        elif jogador2ganhou and not jogador1ganhou:
            print("jogador 2 ganhou")

jogo = Tabuleiro()
jogo.adicionar_barco(True,(2,2))
jogo.adicionar_barco(False,(2,2))
jogo.atacar(True,(2,2))