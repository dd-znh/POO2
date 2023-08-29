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
    def __init__(self, notas):
        pass