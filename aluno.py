class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def __str__(self):
        return f"A media do aluno {self.nome} eh: {self.calcular_media()}"

a1 = Aluno('Ana Paula', 13, 25)
print(f"{a1}")