#1, 2
from typing import Any


class Lista():
    def __init__(self, vetor:list):
        self.__vetor = vetor

    @property
    def vetor(self):
        return self.__vetor

    @vetor.setter
    def vetor(self, vetor:list):
        self.__vetor = vetor 
    
    def inv(self):
        for i in self.vetor:
            return self.vetor[::-1]
        
v1 = Lista([1, 2, 3, 4, 5])
print(v1.vetor)
v1.vetor = [1, 2, 3]
print(v1.vetor)
print(v1.inv())

# 3
class Nota():
    def __init__(self, nota):
        self.__nota = nota

    @property
    def nota(self):
        return(self.__nota)
    
    @nota.setter
    def nota(self, nota):
        self.__nota = nota

class Media():
    def __init__(self, n1:Nota, n2:Nota, n3:Nota, n4:Nota):
        self.media = (n1.nota+n2.nota+n3.nota+n4.nota) / 4

n1 = Nota(5)
n2 = Nota(7)
n3 = Nota(2)
n4 = Nota(3)
m1 = Media(n1, n2, n3, n4)
print(m1.media)

class Nota():
    def __init__(self, nota):
        self.nota = nota

class Media():
    def __init__(self, n1:Nota, n2:Nota, n3:Nota, n4:Nota):
        self.media = (n1.nota+n2.nota+n3.nota+n4.nota) / 4

n1 = Nota(5)
n2 = Nota(7)
n3 = Nota(2)
n4 = Nota(3)
m1 = Media(n1, n2, n3, n4)
print(m1.media)

#5
class VetNum():
    def __init__(self, vetor: list):
        self.__vetor = vetor

    @property
    def vetor(self):
        return self.__vetor

    @vetor.setter
    def vetor(self, vetor):
        self.__vetor = vetor

    def SepParImpar(self):
        if len(self.__vetor) == 20:
            par = []
            impar = []
            for numero in self.__vetor:
                if numero % 2 == 0:
                    par.append(numero)
                else:
                    impar.append(numero)
            return self.__vetor, impar, par

l1 = VetNum([1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(l1.SepParImpar())

#6
class Aluno():
    def __init__(self, nome, notas: list):
        self.nome = nome
        self.__notas = notas
        self.media = 0
    
    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, notas):
        self.__notas = notas

    def CalcMedia(self):
        for nota in self.__notas:
            self.media += nota
        self.media = ("%.2f" % (self.media / len(self.__notas)))

class Sistema:
    def __init__(self, lista_alunos):
        self.__lista_alunos = lista_alunos

    @property
    def lista_alunos(self):
        return self.__lista_alunos

    @lista_alunos.setter
    def lista_alunos(self, aluno):
        self.__lista_alunos.append(aluno)

    def excluir_aluno(self, aluno:Aluno):
        self.__lista_alunos.remove(aluno)

    def check(self):
        for aluno in self.__lista_alunos:
            if float(aluno.media) >= 7:
                print("O aluno", aluno.nome, "passou com", aluno.media)
            else:
                print("O aluno", aluno.nome, "reprovou com a nota", aluno.media)
   
x = Aluno("Pedro", [3, 5, 6, 9])
x2 = Aluno("Rodolfo", [7, 7, 7, 8])
y = Sistema([x, x2])
x.CalcMedia()
x2.CalcMedia()
print(x.media)
y.check()

# 8
class Pessoas:
    def __init__(self, nome:list, idade:list, altura:list):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def altura(self):
        return self.__altura
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    @altura.setter
    def altura(self, altura):
        self.__altura = altura
    
    def infos(self):
        print(self.__nome[::-1])
        print(self.__idade[::-1])
        print(self.__altura[::-1])

x = Pessoas(["joao", "pedro"], [10, 11], [170, 172])
x.infos()

# 9
class Vetor:
    def __init__(self, vetor):
        self.__vetor = vetor
    
    @property
    def vetor(self):
        return self.__vetor
    
    @vetor.setter
    def vetor(self, vetor):
        self.__vetor = vetor
    
    def sumOfSquares(self):
        somador = 0
        for element in self.__vetor:
            somador += element**2
        print(somador)

x = Vetor([1, 2, 3])
x.sumOfSquares()

# 10
class Vetores:
    def __init__(self, vet1, vet2, vet3):
        self.__vet1 = vet1
        self.__vet2 = vet2
        self.__vet3 = vet3

    @property
    def vet1(self):
        return self.__vet1

    @property
    def vet2(self):
        return self.__vet2
    
    @property
    def vet3(self):
        return self.__vet3
    
    @vet1.setter
    def vet1(self, vet1):
        self.__vet1 = vet1
    
    vet2.setter
    def vet2(self, vet2):
        self.__vet2 = vet2
    
    vet3.setter
    def vet3(self, vet3):
        self.__vet3 = vet3

    def mesclar(self):
        vet_prin = []
        for i in range(len(self.__vet1)):
            vet_prin.append(self.__vet1[i])
            vet_prin.append(self.__vet2[i])
            vet_prin.append(self.__vet3[i])
        print(vet_prin)

x = Vetores([1, 2, 3], [4, 5, 6], [7, 8, 9])
x.mesclar()