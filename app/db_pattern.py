from sqlite3 import *


def tb_student(vsql):
    vsql.execute('''CREATE TABLE aluno
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL,
    SOBRENOME TEXT NOT NULL )''')


def tb_classroom(vsql):
    vsql.execute('''CREATE TABLE sala_aula
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL,
    CAPACIDADE INTEGER NOT NULL)''')


def tb_coffee_room(vsql):
    vsql.execute('''CREATE TABLE sala_cafe
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL)''')


def main():
    conn = connect('tb_app.db')
    c = conn.cursor()
    tb_student(c)
    tb_classroom(c)
    tb_coffee_room(c)




main()
