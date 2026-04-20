import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="asibd",
        password="asibd#12",
        database="escolas_bd"
    )