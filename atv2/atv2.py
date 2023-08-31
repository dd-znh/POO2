#1 e 2
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

#3
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

#4
class Palavra():
    def __init__(self, palavra: str):
        self.__palavra = palavra
    
    @property
    def palavra(self):
        return self.__palavra

    @palavra.setter
    def palavra(self, palavra):
        self.__palavra = palavra
    
    def printConsoante(self):
        cont_consoante = 0
        vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        for letra in self.__palavra:
            if letra not in vogais:
                cont_consoante += 1
        return cont_consoante

p1 = Palavra("batatao")
print(p1.printConsoante())

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
        par = []
        impar = []
        for numero in self.__vetor:
            if numero % 2 == 0:
                par.append(numero)
            else:
                impar.append(numero)
        return self.__vetor, impar, par

l1 = VetNum([1 ,2, 3, 4, 5, 6, 7, 8])
print(l1.SepParImpar())
l1.vetor = [1, 2, 3]
print(l1.vetor)

#6
class Aluno():
    def __init__(self, notas: list):
        self.__notas = notas
        self.__media = 0
    
    @property
    def notas(self):
        return self.__notas

    @notas.setter
    def notas(self, notas):
        self.__notas = notas
    
    @property
    def media(self):
        return self.__media

    @media.setter
    def media(self, media):
        self.__media = media
    
    def CalcMedia(self):
        for nota in self.__notas:
            self.__media += nota
        self.__media = ("%.2f" % (self.__media / len(self.__notas)))

x = Aluno([3, 5, 6, 9])
x.CalcMedia()
print(x.media)

#falta terminar o exercício...