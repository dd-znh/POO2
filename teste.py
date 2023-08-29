class Livro:
    def __init__(self, codigo: int, titulo: str, ano: int, editora, autor, numeroCapitulo: int, tituloCapitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__editora = editora
        self.__autores = [autor]
        self.__numeroCapitulo = [numeroCapitulo]
        self.__tituloCapitulo = [tituloCapitulo]

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def ano(self):
        return self.__ano

    @property
    def editora(self):
        return self.__editora

    @property
    def autores(self):
        return self.__autores

    @property
    def numeroCapitulo(self):
        return self.__numeroCapitulo

    @property
    def tituloCapitulo(self):
        return self.__tituloCapitulo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @codigo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @autores.setter
    def autores(self, autor):
        self.__autores = [autor]

    @numeroCapitulo.setter
    def numeroCapitulo(self, numeroCapitulo):
        self.__numeroCapitulo = [numeroCapitulo]

    @tituloCapitulo.setter
    def tituloCapitulo(self, tituloCapitulo):
        self.__tituloCapitulo = [tituloCapitulo]

    def incluirAutor(self, autor):
        if isinstance(autor, Autor) and autor not in self.__autores:
            self.__autores.append(autor)

    def excluirAutor(self, autor):
        if autor in self.__autores:
            self.__autores.remove(autor)

    def incluirCapitulo(self, numeroCapitulo: int, tituloCapitulo: str):
        if numeroCapitulo not in self.__numeroCapitulo and tituloCapitulo not in self.__numeroCapitulo:
            self.__numeroCapitulo.append(numeroCapitulo)
            self.__tituloCapitulo.append(tituloCapitulo)

    def excluirCapitulo(self, tituloCapitulo: str):
        for i in range(len(self.__tituloCapitulo)):
            if tituloCapitulo == self.__tituloCapitulo[i]:
                self.__tituloCapitulo.remove(tituloCapitulo)
                self.__numeroCapitulo.pop(i)

    def findCapituloByTitulo(self, tituloCapitulo: str):
        for i in range(len(self.__tituloCapitulo)):
            if tituloCapitulo == self.__tituloCapitulo[i]:
                return self.tituloCapitulo[i]
            
class Biblioteca:
    def __init__(self):
        self.__livros = []

    def incluirLivro(self, livro: Livro):
        if isinstance(livro, Livro) and livro not in self.__livros:
            self.__livros.append(livro)

    def excluirLivro(self, livro: Livro):
        if livro in self.__livros:
            self.__livros.remove(livro)

    @property
    def livros(self):
        return self.__livros

class Capitulo:
    def __init__(self, numero: int, titulo: str):
        self.__numero = numero
        self.__titulo = titulo

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

class Editora:
    def __init__(self, codigo: int, nome: str):
        self.__codigo = codigo
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nome(self):
       return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

class Autor:
    def __init__(self, codigo: int, nome: str):
        self.__codigo = codigo
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
