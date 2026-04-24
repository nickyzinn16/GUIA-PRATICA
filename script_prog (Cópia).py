from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, name=None, email=None, id=None):
        self.name = name
        self.email = email
        self.id = id

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    def __str__(self):
        return f"{self.name} ({self.get_type()})"

    
    #getter
    @property
    def id(self):
        return self.__id

    #setter
    @id.setter
    def id(self, value):
        if value < 0:
            raise ValueError("Este valor nao eh permitido")
        self.__id = value

    @abstractmethod
    def get_type(self):
        pass



class Aluno(Pessoa):
    def __init__(self, name=None, email=None, id=None, notas=None):
        super().__init__(name, email, id)
        self.notas = notas

# - - - - - 
    @property
    def notas(self):
        return self._notas

    @notas.setter
    def notas(self, lista_notas):
        for nota in lista_notas:
            if nota < 0 or nota > 20:
                raise ValueError("As notas devem estar entre 0 e 20")
        self._notas = lista_notas

# - - - - - 


    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def get_type(self):
        return "Aluno da escola"

    def get_description(self):
        return f"O aluno {self.name}, tem média de {self.calcular_media():.2f}"


class Pussor(Pessoa):
    def __init__(self, name=None, email=None, id=None, subject=None):
        super().__init__(name, email, id)
        self.subject = subject

    def get_subjcts(self):
        return self.subject

    def get_type(self):
        return "Professor da escola"

    def get_description(self):
        return f"O professor {self.name}, leciona {self.subject}."

    if __name__ == "__main__":
    # Processamento do Aluno
    print("ok")
    aluno1 = Aluno("Mario Santos", "msantos@gmail.com", 12, [15, 10, 13])
    aluno2 = Aluno("Kylian Mbappe", "kmbappe@gmail.com", 18, [10, 10, 20])
    aluno3 = Aluno("Lamine Yamal", "lyamal@gmail.com", 10, [15, 10, 12])
    prof1 = Pussor("Pep Guardiola", "guardola@gmail.com", 10, "Tiki taka")
    prof2 = Pussor("Jose Mourinho", "mourinho@gmail.com", 10, "Retranca Total")

    pessoas = [aluno1, aluno2, aluno3, prof1, prof2]

    for pessoa in pessoas:
        print(pessoa)

    for pessoa in pessoas:
        print(pessoa.get_description())

    
    # Processamento do Professor TRAZER INTERACAO COM BASE DE DADOS ATRAVES DE HERANCA E POLIMOFIRMO


class Funcionarios(Pessoa):
    def __init__(self, name=None, email=None, area=None, tipo=None, id=None):
        super().__init__(name, email, area, tipo, id)

    def get_type(self):
        return "Funcionario da escola"

    def adicionar_funcionaro(self):
        conn = conectar()
        cursor = conn.cursor()

        sql = "INSERT INTO funcionarios (nome, email, area, tipo) VALUES (%s, %s, %s, %s)"
        valores = (self.name, self.email, self.area, self.tipo)

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

    # ======================================================================================================
    # ======================================================================================================
    # ======================================================================================================