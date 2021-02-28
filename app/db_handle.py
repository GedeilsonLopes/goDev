from sqlite3 import *
from sqlite3 import Error
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

database = 'app/tb_app.db'


def connect_db():
    """Estabelece a conexão com o banco de dados."""

    conn = connect(database)
    return conn


def dql(query):
    """Realiza as operações de SELECT dentro do banco
    """
    try:
        vconn = connect_db()
        c = vconn.cursor()
        c.execute(query)
        q_result = c.fetchall()
        vconn.close()
        return q_result
    except Error as ex:
        print(ex)


def dml(query):
    """Realiza as operações de INSERT, UPDATE e DELETE dentro do banco"""
    try:
        vconn = connect_db()
        c = vconn.cursor()
        c.execute(query)
        vconn.commit()
        vconn.close()
    except Error as ex:
        print(ex)


def insert_student(name, surname):
    """Insere dados na tabela aluno"""

    v_name = name.get()
    v_surname = surname.get()

    try:
        if v_name and v_surname:
            vquery = f"INSERT INTO aluno(NOME, SOBRENOME) VALUES ('{v_name}', '{v_surname}')"
            dml(vquery)
        else:
            tk.messagebox.showerror('Entrada inválida', 'Digite um valor válido')
    except Error as ex:
        tk.messagebox.showerror('Erro', ex)

    name.delete(first=0, last='end')
    surname.delete(first=0, last='end')


def insert_classroom(name, capacity):
    """Insere dados na tabela sala_aula"""

    v_name = name.get()
    v_capacity = capacity.get()

    try:
        if v_capacity.isdigit():
            int_capacity = int(v_capacity)
            if v_name != '' and int_capacity > 0:
                vquery = f"INSERT INTO sala_aula(NOME, CAPACIDADE) VALUES ('{v_name}', {int_capacity})"
                dml(vquery)
        else:
            tk.messagebox.showerror('Entrada inválida', 'Digite um valor válido')

    except Error as ex:
        tk.messagebox.showerror('Erro', ex)

    name.delete(first=0, last='end')
    capacity.delete(first=0, last='end')


def insert_coffee_room(name1, name2):
    """Insere dados na tabela sala_cafe"""

    v_name1 = name1.get()
    v_name2 = name2.get()

    try:

        if v_name1 and v_name2:
            vquery = f"INSERT INTO sala_cafe(NOME) VALUES ('{v_name1}')"
            dml(vquery)
            vquery = f"INSERT INTO sala_cafe(NOME) VALUES ('{v_name2}')"
            dml(vquery)
        else:
            tk.messagebox.showerror('Entrada inválida', 'Digite um valor válido')

    except Error as ex:
        tk.messagebox.showerror('Erro', ex)

    name1.delete(first=0, last='end')
    name2.delete(first=0, last='end')


# Gerador de dados de pesquisa

def search_student():
    vquery = f"SELECT * FROM aluno"
    result = dql(vquery)
    student_list = []
    for student in result:
        student_list.append(f'{student[1].capitalize()} {student[2].capitalize()}')
    return student_list


def search_classroom():
    vquery = f"SELECT * FROM sala_aula"
    result = dql(vquery)
    classroom_list = []
    for room in result:
        classroom_list.append(room)
    return classroom_list


def search_coffee_room():
    vquery = f"SELECT * FROM sala_cafe"
    dql(vquery)
    result = dql(vquery)
    coffee_room_list = []
    for room in result:
        coffee_room_list.append(room)
    return coffee_room_list


def classroom_fill():
    std = search_student()
    cls = search_classroom()
    cls_total_cap = 0
    for classroom in cls:
        cls_total_cap += classroom[2]
    if cls_total_cap < len(std):
        return tk.messagebox.showerror('Erro',
                                       'Capacidade das salas menor que o número de alunos. Por favor, adicione mais '
                                       'salas.')
    else:
        cls_filled = len(std) // len(cls)
    return cls_filled


# Define os alunos presentes em cada etapa do curso
def classroom_listing():
    cls = search_classroom()
    std = search_student()
    cls_limit = classroom_fill()
    first_classes = {}
    second_classes = {}

    # Etapa 1 do curso
    for rev_room in cls:
        empty_room = []
        for i in range(cls_limit):
            empty_room.append(std[0])
            std.pop(0)
        first_classes[f'{rev_room[1]}'] = empty_room.copy()
        empty_room.clear()

    # Etapa 2 co curso
    for rev_room in cls:
        transfer_students = []
        empty_room_2 = []
        for v in first_classes.values():
            for i in range(len(v) // 2):
                transfer_students.append(v[i])

        for rev_room in reversed(cls):
            for i in range(cls_limit // 2):
                empty_room_2.append(transfer_students[0])
                transfer_students.pop(0)
            second_classes[f'{rev_room[1]}'] = empty_room_2.copy() + first_classes[f'{rev_room[1]}'][cls_limit // 2:]
            empty_room_2.clear()

    return first_classes, second_classes


# Define aleatoriamente onde os alunos ficarão em cada intervalo
def coffee_room_listing():
    std_1 = search_student()
    std_2 = search_student()
    cof = search_coffee_room()
    cof_cap = len(std_1) // 2
    coffee_1 = {}
    coffee_2 = {}

    for room in cof:
        empty_room = []
        for i in range(cof_cap):
            empty_room.append(std_1[0])
            std_1.pop(0)
        coffee_1[f'{room[1]}'] = empty_room.copy()
        empty_room.clear()

    for room in cof:
        empty_room = []
        for i in range(cof_cap):
            empty_room.append(std_2[-1])
            std_2.pop()
        coffee_2[f'{room[1]}'] = empty_room.copy()
        empty_room.clear()

    return coffee_1, coffee_2


# informa os alunos presentes nos espaços de café em cada intervalo

def info_coffee(coffee_room):
    cof = coffee_room_listing()
    info_cof = [coffee_room]

    for room in cof:
        for k in room.keys():
            if coffee_room == k:
                info_cof.append(room[k])
    return info_cof


# Informa os dados de cada aluno
def info_student(student):
    cls = classroom_listing()
    cof = coffee_room_listing()
    std_info = [student]

    for stage in cls:
        for k, v in stage.items():
            if student in v:
                std_info.append(k)

    for room in cof:
        for k, v in room.items():
            if student in v:
                std_info.append(k)

    return std_info

def info_class(classroom):
    cls = classroom_listing()
    info_cls = [classroom]

    for c in cls:
        for k in c.keys():
            if classroom == k:
                info_cls.append(c[k])
    return info_cls
print(info_class('Diferenciados'))

def search_btn_press(master, variable, entry):
    value = variable.get()
    entry = entry.get()
    if entry != '':
        if value == 'a':
            info = info_student(entry)
            trv = ttk.Treeview(master, columns=('Nome', 'Etapa 1', 'Etapa 2', 'Intervalo 1', 'Intervalo 2'), show='headings')
            trv.column('Nome', width=70)
            trv.column('Etapa 1', width=74)
            trv.column('Etapa 2', width=74)
            trv.column('Intervalo 1', width=74)
            trv.column('Intervalo 2', width=74)
            trv.heading('Nome', text='Nome')
            trv.heading('Etapa 1', text='Etapa 1')
            trv.heading('Etapa 2', text='Etapa 2')
            trv.heading('Intervalo 1', text='Café 1')
            trv.heading('Intervalo 2', text='Café 2')
            trv.place(x=410, y=130, width=370, height=450)
            trv.insert('', 'end', values=info)
            return trv

        elif value == 'c':
            info = info_class(entry)
            trv = ttk.Treeview(master, columns=('Nome', 'Etapa 1', 'Etapa 2'),
                               show='headings')
            trv.column('Nome', width=123)
            trv.column('Etapa 1', width=123)
            trv.column('Etapa 2', width=123)
            trv.heading('Nome', text='Nome')
            trv.heading('Etapa 1', text='Etapa 1')
            trv.heading('Etapa 2', text='Etapa 2')
            trv.place(x=410, y=130, width=370, height=450)
            trv.insert('','end',value= info[0])
            for person in info[1]:
                trv.insert('','end',value=('',person))
            for person in info[2]:
                trv.insert('', 'end', value=('', '',person))
            return trv

        elif value == 'r':
            info = info_coffee(entry)
            trv = ttk.Treeview(master, columns=('Nome', 'Intervalo 1', 'Intervalo 2'),
                               show='headings')
            trv.column('Nome', width=123)
            trv.column('Intervalo 1', width=123)
            trv.column('Intervalo 2', width=123)
            trv.heading('Nome', text='Nome')
            trv.heading('Intervalo 1', text='Café 1')
            trv.heading('Intervalo 2', text='Café 2')
            trv.place(x=410, y=130, width=370, height=450)
            trv.insert('', 0, value=info[0])
            for person in info[1]:
                trv.insert('', 'end', value=('', person))
            for person in info[2]:
                trv.insert('', 'end', value=('', '', person))
            return trv
        else:
            tk.messagebox.showerror('Erro', 'Selecione alguma opção de pesquisa')
    else:
        tk.messagebox.showerror('Erro', 'Objeto da pesquisa inválido')




