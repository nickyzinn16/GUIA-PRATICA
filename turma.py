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

class Funcionarios:
       def inserir_funcionarios(self, funcionarios):
        conn = conectar()
        cursor = conn.cursor()

        sql = "INSERT INTO funcionarios (nome, email, area, tipo) VALUES (%s, %s, %s, %s)"
        valores = (funcionarios.nome, funcionarios.email, funcionarios.area, funcionarios.tipo)

        cursor.execute(sql, valores)
        conn.commit()

        cursor.close()
        conn.close()

    # ======================================================================================================
    # ======================================================================================================
    # ======================================================================================================

    def listar_funcionarios(self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome, email, area, tipo FROM funcionarios")
        result_query = cursor.fetchall()

        lista_funcionarios = []

        for nome, email, area, tipo in result_query:
            funcionarios = {
                "nome": nome,
                "email": email,
                "area": area,
                "tipo": tipo
            }

            lista_funcionarios.append(funcionarios)

        cursor.close()
        conn.close()

        return lista_funcionarios
