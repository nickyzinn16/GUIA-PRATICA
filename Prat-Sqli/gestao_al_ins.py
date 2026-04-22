from db import conectar

class AlunoI:

    def __init__(self, id):
        self.id = id

    def selecionar_dados_inseguro(self):
        query = f"SELECT * FROM alunos WHERE id = {self.id}"

        conn = conectar()

        cursor = conn.cursor()
        cursor.execute(query)

        resultado_alunos = cursor.fetchall()
        conn.close()

        print (f"Resultado Alunos: {resultado_alunos}")
        return resultado_alunos


    def selecionar_dados_seguro(id):
        query = "SELECT * FROM alunos WHERE id = %s"

        conn = conectar()

        cursor = conn.cursor()
        cursor.execute(query, (id))

        resultado_alunos = cursor.fetchall()
        conn.close()

        print (f"Resultado Alunos: {resultado_alunos}")
        return resultado_alunos

payload = "1900 or 1 = 1"
al01 = AlunoI(payload)
al01.selecionar_dados_inseguro() 

