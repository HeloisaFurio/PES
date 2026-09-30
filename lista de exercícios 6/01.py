class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def apresentar(self):
        print(f"{self.titulo} foi escrito por {self.autor}")

BTM = Livro("Melhor do que nos filmes", "Lynn Painter")
PNA = Livro("Patinando no Amor", "Lynn Painter")
CEND = Livro("Confiando em Nós Dois", "Lynn Painter")

BTM.apresentar()
PNA.apresentar()
CEND.apresentar()