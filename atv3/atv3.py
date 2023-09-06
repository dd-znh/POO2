# 1 e 2
import string
from typing import Any
class Texto:
    def __init__(self, texto):
        self.__texto = texto.lower()
        self.__dic = {}

    @property
    def texto(self):
        return self.__texto
    
    @texto.setter
    def texto(self, texto):
        self.__texto = texto

    @property
    def dic(self):
        return self.__dic
    
    @dic.setter
    def dic(self, dic):
        self.__dic = dic

    def contador_palavra(self):
        tabela_de_traducao = str.maketrans('', '', string.punctuation)
        texto_traduzir = self.__texto.translate(tabela_de_traducao)
        texto_traduzir = (texto_traduzir).split()
        for palavra in texto_traduzir:
            if palavra not in self.__dic:
                self.__dic[palavra] = 1
            else:
                self.__dic[palavra] += 1
    
    def del_stop_words(self):
        new_dic = {}
        with open('atv3/stopwords.txt', 'r') as arquivo:
            lista_de_palavras = arquivo.read().splitlines()
            for chave in self.__dic.keys():
                if chave not in lista_de_palavras:
                    new_dic[chave] = self.__dic[chave]
            self.__dic = new_dic
            return self.__dic

t1 = Texto("a casa era uma casa, era uma casa casa")
t1.contador_palavra()
print(t1.texto)
print(t1.dic)
print(t1.del_stop_words())

# 3
class Aluno:
    def __init__(self, nome:str, nota1:float, nota2:float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = (nota1 + nota2) / 2

class Sistema:
    def __init__(self):
        self.__dados = {}
    
    def adicionar_aluno(self, aluno:Aluno):
        if aluno not in self.__dados:
            self.__dados[aluno.nome] = (aluno.nota1, aluno.nota2)
    
    def remover_aluno(self, aluno:Aluno):
        if aluno in self.__dados:
            self.__dados.pop(aluno)
    
    def retornar_dicionario(self):
        return self.__dados
    
# 4
class Corredor:
    def __init__(self, nome, lista_tempos:list):
        self.nome = nome
        self.lista_tempos = lista_tempos
        self.tempo_total = 0
        for tempo in lista_tempos:
            self.tempo_total += tempo

    def adicionar_tempo(self, tempo):
        self.lista_tempos.append(tempo)
    
    def remover_tempo(self, tempo):
        self.adicionar_tempo.pop(tempo)
    
class Corrida:
    def __init__(self, lista_corredores:list):
        self.dados = {}
        for corredor in lista_corredores:
            self.dados[corredor.nome] = corredor.tempo_total

    def declarar_placar(self):
        for i in sorted(self.dados, key = self.dados.get):
            return i, self.dados[i]
        
# 5
# Em relação ao que foi proposto, fiz as seguintes modificações:
# A função incluir telefone foi colocada na classe pessoa
# A função incluir telefone ja esta automaticamente ligada, dessa forma, a
# uma pessoa. A alteração foi feita pois na minha visão faz mais sentido
# modelar dessa forma.
class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = []
        self.telefone.append(telefone)
    
    def incluir_telefone(self, telefone):
        self.telefone.append(telefone)
    
    def excluir_telefone(self, telefone):
        self.telefone.remove(telefone)
    
    def consultar_numeros(self):
        print(self.telefone)

class Agenda:
    def __init__(self):
        self.dicionario = {}
    
    def incluir_nova_pessoa(self, pessoa:Pessoa):
        self.dicionario[pessoa.nome] = pessoa.telefone # lista de numeros...
    
    def procurar_pessoa(self, pessoa:Pessoa):
        if pessoa in self.dicionario:
            return self.dicionario[pessoa]
        else:
            return "Pessoa não está no dicionário"
    
    def excluir_pessoa(self, pessoa:Pessoa):
        if pessoa in self.dicionario:
            self.dicionario.pop(pessoa)
    
    def consultar_telefone(self, pessoa:Pessoa):
        if pessoa.nome in self.dicionario:
            print(self.dicionario[pessoa.nome])
        else:
            print("Pessoa não encontrada")
        
pes1 = Pessoa("Eduardo", 123)
ag = Agenda()
pes1.incluir_telefone(123)
pes1.excluir_telefone(123)
pes1.incluir_telefone(321)
ag.incluir_nova_pessoa(pes1)
pes1.consultar_numeros()
ag.consultar_telefone(pes1)
