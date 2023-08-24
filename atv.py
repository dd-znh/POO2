from typing import Any
import math
import random
import numpy as np

#1

class Cliente(): # classe cliente e seus atributos
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

class Conta(): # classe conta e seus atributos
    def __init__(self, titulares:list, premium:bool):
        self.titulares = titulares
        self.saldo = 0
        self.dados = []
        self.premium = premium # conta sem limite de cheque especial
        for obj in titulares:
            self.dados.append((obj.nome, obj.telefone)) # matriz dos dados dos titulares
        self.extrato = [] # armazena tuplas com saldo antes da operacao, saldo depois da operacao e operacao 
        
    def deposito(self, valor): # nao se pode depositar valores negativos
        if valor > 0:
            self.extrato.append((self.saldo, self.saldo + valor, "deposito"))
            self.saldo += valor
        else:
            print("operacao indisponivel")

    def saque(self, valor): # nao se pode sacar valores "positivos"
        if (self.saldo - valor >= 0 or self.premium) and valor > 0:
            self.extrato.append((self.saldo, self.saldo - valor, "saque"))
            self.saldo -= valor
        else:
            print("operacao indisponivel")

    def print_saldo(self): # metodo para printar saldo
        print("seu saldo é de", self.saldo)

    def print_titulares(self): # metodo para printar matriz dos dados dos titulares
        print(self.dados)
    
    def print_extrato(self): # metodo para printar lista do extrato
        print(self.extrato)

p1 = Cliente("pedrinho", 12345678910, 48991522161) # criacao de objetos para teste
p2 = Cliente("joaozinho", 10987654321, 4898843991010)
c1 = Conta([p1, p2], False)
c2 = Conta([p1], True)
c1.deposito(500)
c1.saque(200)
c1.saque(400)
c2.deposito(100)
c1.print_saldo()
c1.print_titulares()
c1.print_extrato()

#2
class Livro(): # classe livro com seus atributos
    def __init__(self, titulo, autores, ano, editora, edicao, volume):
        self.id = id
        self.titulo = titulo
        self.autores = autores
        self.ano = ano
        self.editora = editora
        self.edicao = edicao
        self.volume = volume

livro1 = Livro("Calculo1", "Stwart", "1500", "edUFSC", 69, 420) # objeto livro

class Biblioteca(): # classe biblioteca com adicao e busca de livros
    def __init__(self, codigo):
        self.codigo = codigo
        self.lista_livros = []
    
    def adicionar_livro(self, id): # adiciono todos os dados do livro em tupla
        info_livro = (id.titulo, id.autores, id.ano, id.editora, id.edicao, id.volume)
        if info_livro not in self.lista_livros:
            self.lista_livros.append(info_livro)
    
    def pesquisar_livro(self, pesquisa): # se existe algum elemento da tupla que bate com a pesquisa printa todas as infos do livro
        for tupla in self.lista_livros:
            for elemento in tupla:
                if elemento == pesquisa:
                    print(tupla)
                
b1 = Biblioteca(1) # exemplificando
b1.adicionar_livro(livro1)
b1.pesquisar_livro("1500")
        

#4

class Numeros: # classe numeros com o respectivo numero como atributo
    def __init__(self, numero: int):
        self.numero = numero
    
    def fibonacci(self): # return da lista da sequencia de fibonacci de len = self.numero
        lista = [1, 1]
        if self.numero == 0:
            pass
        elif self.numero == 1:
            return(1)
        else:
            for i in range(self.numero-2):
                lista.append(int((lista[len(lista)-2])+(lista[len(lista)-1])))
            return(lista)
    
    def fatorial(self): # return do numero fatorial
        x = 1
        for i in range(self.numero):
            x *= i+1
        return x
    
a = Numeros(7) # criacao de objetos, e print do return dos metodos
b = Numeros(3)

print(a.fibonacci())
print(b.fatorial())

#6
#informações importantes de um baralho: valor, naipe, figura

class Baralho(): # classe baralho
    def __init__(self):
        self.figura = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # valor pode variar dependendo do jogo, porem padronizado para a maioria dos jogos
        self.naipe = ["c", "p", "e", "o"] #copas, paus, espadas, e ouros respec/
        self.cartas = [] # lista para armazenamento do baralho criado
        for figuras in self.figura:
            for naipes in self.naipe:
                self.cartas.append((figuras, naipes))
        
B1 = Baralho() # criacao do baralho
print(B1.cartas) # print do baralho

#8

class Forca(): # classe forca com seus respectivos atributos
    def __init__(self, gabarito: str):
        self.gabarito = gabarito
        self.jogo = ["_"] * len(self.gabarito)
        self.vida = 5
        print(self.jogo)
    
    def testar_letra(self, letra): # metodo para testar se a letra pertence a palavra, se sim mostra ela no self.jogo, senao perde uma vida
        perder_vida = True
        for i in range (len(self.gabarito)):
            if letra == self.gabarito[i]:
                self.jogo[i] = letra
                perder_vida = False
        if perder_vida == True:
            self.vida -= 1
            print("voce perdeu uma vida e esta com", self.vida, "vidas")
        print(self.jogo)
        self.resposta()
    
    def resposta(self): # metodo para conferir se acabou o numero de vidas
        if self.vida == 0:
            print("Parabens, voce perdeu")
        elif not "_" in self.jogo:
            print("Voce ganhou, que pena")
    
forca1 = Forca("batata") # jogo teste 
forca1.testar_letra("a")
forca1.testar_letra("b")
forca1.testar_letra("x")
forca1.testar_letra("t")

# 10

class Pessoas(): # superclasse pessoa para incluir professor e alunos
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
class Turmas(): # classe turmas com atributos (lista de alunos pois sao varios alunos e apenas um professoer)
    def __init__(self, aula, codigo, professor):
        self.aula = aula
        self.codigo = codigo
        self.alunos = []
        self.professor = professor
    
    def adicionar_aluno(self, matricula): # metodo para adicionar a matricula do aluno na lista da sala
        if matricula not in self.alunos:
            self.alunos.append(matricula)
            print("Aluno adicionado a turma com sucesso")
        else:
            print("Esse aluno já está nessa turma")

    def remover_aluno(self, matricula): # metodo para remover matricula do aluno da lista da sala
        if matricula in self.alunos:
            self.alunos.remove(matricula)
            print("Aluno removido da turma com sucesso")
        else:
            print("Esse aluno não está nessa turma")

    def mostrar_dados_turma(self): # metodo para printar atributos da turma
        print(self.aula, self.codigo, self.alunos, self.professor)

    def adicionar_falta(self, aluno): # metodo para adicionar falta no atributo do aluno se a matricula estiver na lista
        if aluno.matricula in self.alunos:
            aluno.falta += 1
        else:
            print("aluno nao esta na turma para sofrer falta")
    
class Alunos(Pessoas): # classe alunos herdando atributos da classe pessoas
    def __init__(self, nome, cpf, matricula, nota, falta):
        super().__init__(nome, cpf)
        self.matricula = matricula
        self.nota = nota
        self.falta = falta
    
    def mostrar_dados_aluno(self): # metodo para printar atributos do aluno
        print(self.cpf, self.matricula, self.nome, self.nota, self.falta)

class Professores(Pessoas): # classe professores herdando atributos da classe pessoa
    def __init__(self, nome, cpf, clt):
        super().__init__(nome, cpf)
        self.clt = clt
    
    def mostrar_dados_professor(self): # metodo para printar atributos do aluno
        print(self.clt, self.cpf, self.nome)

a1 = Alunos("Eduardo", "123456789-10", "23123456", 8.5, 1) # criando objetos e testando metodos
p1 = Professores("Joelinton", "109876543-21", "001")
aula1 = Turmas("POO", 1234, p1)
aula1.adicionar_aluno(a1.matricula)
aula1.remover_aluno(a1.matricula)
a1.mostrar_dados_aluno()
aula1.mostrar_dados_turma()
aula1.adicionar_falta(a1)
a1.mostrar_dados_aluno()


# 9 Campo Minado
# O jogo possuirá 3 matrizes, uma do jogo onde oculta todos os blocos que nao foram "jogados"
# Uma com o as bombas e o numero de bombas proximas por bloco
# E outra apenas com as bombas, que sera utilizada como base para a montagem da 2a
class CampoMinado():
    def __init__(self, tamanho, bombas):
        self.tamanho = tamanho
        self.bombas = bombas

        self.jogo = [None] * (self.tamanho + 2)
        for i in range((self.tamanho+2)):
            self.jogo[i] = [False] * (self.tamanho + 2)

        self.gab_jogo = [None] * self.tamanho
        for i in range(self.tamanho):
            self.gab_jogo[i] = [None] * self.tamanho

        self.comp_jogo = [None] * self.tamanho
        for i in range(self.tamanho):
            self.comp_jogo[i] = ["_"] * (self.tamanho)
        self.add_bombas()

    def add_bombas(self): # adicionando bombas com coordenadas aleatorias na 1a matriz
        somador_add_bombas = 0
        while somador_add_bombas < self.bombas:
            random_number1 = random.randint(1, self.tamanho)
            random_number2 = random.randint(1, self.tamanho)
            if self.jogo[random_number1][random_number2] == False:
                self.jogo[random_number1][random_number2] = True
                somador_add_bombas += 1
        self.gabarito()

    def gabarito(self): # adicionando o numero de bombas proximas a coordenada e onde tem bomba na 2a matriz
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                cont_bombas = 0
                if self.jogo[i+1][j+1] == True:
                    self.gab_jogo[i][j] = "b"
                else:
                    if self.jogo[i+1][j] == True:
                        cont_bombas += 1
                    if self.jogo[i+1][j+2] == True:
                        cont_bombas += 1
                    if self.jogo[i][j+1] == True:
                        cont_bombas += 1
                    if self.jogo[i+2][j+1] == True:
                        cont_bombas += 1
                    if self.jogo[i][j] == True:
                        cont_bombas += 1
                    if self.jogo[i+2][j+2] == True:
                        cont_bombas += 1
                    if self.jogo[i][j+2] == True:
                        cont_bombas += 1
                    if self.jogo[i+2][j] == True:
                        cont_bombas += 1
                    self.gab_jogo[i][j] = str(cont_bombas)
        self.jogada()
    
    def jogada(self): # recebendo coordenadas do jogador e caso nao seja a bomba passando o numero para a 3a matriz
        for i in range(self.tamanho):
            print(self.comp_jogo[i])
        chute0, chute1 = input("digite as coordenadas onde voce quer jogar:").split()
        chute0 = int(chute0)
        chute1 = int(chute1)
        if chute0 == chute1 == 0:
            self.print_gabarito()
        elif self.gab_jogo[chute0-1][chute1-1] == "b":
            print("voce perdeu")
            self.print_gabarito()
        else:
            self.comp_jogo[chute0-1][chute1-1] = self.gab_jogo[chute0-1][chute1-1]
            self.resultado()
    
    def print_gabarito(self): # printando 2a matriz
        for i in range(self.tamanho):
            print(self.gab_jogo[i])

    def resultado(self): # caso sobre apenas bombas na 3a matriz o jogador venceu
        num_tracos = 0
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if self.comp_jogo[i][j] == "_":
                    num_tracos += 1
        if num_tracos == self.bombas:
            print("voce venceu")
            self.print_gabarito()
        else:
            self.jogada()

#jogo0 = CampoMinado(3, 1) # teste
#jogo1 = CampoMinado(9, 10) # facil
#jogo2 = CampoMinado(16, 40) # medio

# 3

class Equacao():
    def __init__(self, coeficientes=list):
        self.coeficientes = coeficientes
        self.grau = len(coeficientes) - 1
        self.len = len(coeficientes)
    
    def print_grau(self):
        print("a equacao é de grau", self.grau)
    
    def achar_valor_y(self, x):
        y = 0
        for i in range(self.len):
            y += (self.coeficientes[i]) * (x ** (self.len - (i + 1)))
        print(y)

    def somar_polinomios(self, obj2):
        minlen = min(len(obj2.coeficientes), len(self.coeficientes))
        maxlen = max(len(obj2.coeficientes), len(self.coeficientes))
        resp = []
        for i in range(minlen):
            resp.append(obj2.coeficientes[i] + self.coeficientes[i])
        for i in range(minlen, maxlen):
            if len(obj2.coeficientes) > len(self.coeficientes):
                resp.append(obj2.coeficientes[i])
            else:
                resp.append(self.coeficientes[i])
        print(np.poly1d(resp))

    def multiplicar_polinomios(self, obj2):
        self.coeficientes = np.poly1d(self.coeficientes)
        obj2.coeficientes = np.poly1d(obj2.coeficientes)
        resultado = np.poly1d(self.coeficientes * obj2.coeficientes)
        print(resultado)


e1 = Equacao([1, -3, 2])
e1.achar_valor_y(1)
e2 = Equacao([4, 3, 2, 1])
e1.somar_polinomios(e2)
e1.multiplicar_polinomios(e2)
