banco_jogos = []
proximo_id = 1

class Jogo:
    def __init__(self, titulo, genero, desenvolvedor, plataforma):
        global proximo_id
        self.id = proximo_id
        self.titulo = titulo
        self.genero = genero
        self.desenvolvedor = desenvolvedor
        self.plataforma = plataforma
        proximo_id += 1

    def to_dict(self):
      
        return {
            "id": self.id,
            "titulo": self.titulo,
            "genero": self.genero,
            "desenvolvedor": self.desenvolvedor,
            "plataforma": self.plataforma
        }