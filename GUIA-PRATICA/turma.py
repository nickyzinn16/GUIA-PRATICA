from db import conectar
from aluno import Aluno

# ======================================================================================================
# ======================================================================================================
# ======================================================================================================

class Turma: 
    def adicionar_aluno(self, aluno):
        conn = conectar()

        cursor = conn.cursor()

        sql = "INSERT INTO alunos (nome, nota1, nota2) VALUES (%s, %s, %s)"
        valores = (aluno.nome, aluno.nota1, aluno.nota2)
        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

    # ======================================================================================================
    # ======================================================================================================
    # ======================================================================================================

    def listar_alunos(self):
        conn = conectar()

        cursor = conn.cursor()

        cursor.execute("SELECT nome, nota1, nota2 FROM alunos")

        result_query = cursor.fetchall()

        lista_alunos = []
        for nome, nota1, nota2 in result_query:
            lista_alunos.append(Aluno(nome, nota1, nota2))

        cursor.close()
        conn.close()

        return lista_alunos

    # ======================================================================================================
    # ======================================================================================================
    # ======================================================================================================

    def calcular_media_turma(self):
            conn = conectar()

            cursor = conn.cursor()

            cursor.execute("SELECT AVG((nota1+nota2)/2) FROM alunos")

            media = cursor.fetchone()

            cursor.close()
            conn.close()
            return media if media else 0.0

    # ======================================================================================================
    # ======================================================================================================
    # ======================================================================================================
