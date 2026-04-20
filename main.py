from db import conectar
from aluno import Aluno
from turma import Turma

turma = Turma()

def menu():
    while True:
        print("\n Menu Principal")
        print("1 - Adicionar Alunos")
        print("2 - Listar Alunos")
        print("3 - Ver media da turma")
        print("0 - Sair do Programa")

        option = input("Por favor escolha uma opcao: ")

        if option == "1":
            nome = input("Nome: ")
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))

            aluno = Aluno(nome, nota1, nota2)
            turma.adicionar_aluno(aluno)

            print("Aluno Adicionado")

        elif option == "2":
            alunos = turma.listar_alunos()

            print("\nLista de Alunos")
            for a in alunos:
                print(a)

        elif option == "3":
            media = turma.calcular_media_turma()
            print(f"Media da turma: {media}")

        elif option == "0":
            print("Programa encerrado.")
            break
            
        else:
            print("Opção inválida")

menu()