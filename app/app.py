from tkinter import *
import db_handle
from tkinter import ttk

db_handle.connect_db()

app = Tk()
app.title('Viewer')

# Define o tamanho e o posicionamento da tela
width, height = (800, 600)
window_width = app.winfo_screenwidth()
window_height = app.winfo_screenheight()
pos_x = int(window_width / 2 - width / 2)
pos_y = int(window_height / 2 - height / 2)
app.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
app.resizable(False, False)

title = Label(app, text='Viewer', font='Arial 40').place(width=800, height=100)

# caixa de pesquisa
search_var = StringVar()
search_bar = Entry(app, width=50, font='Arial 10')
search_bar.place(x=10, y=130)
rb_student = Radiobutton(app, text='Aluno', variable=search_var, value='a')
rb_student.place(x=10, y=160)
rb_classroom = Radiobutton(app, text='Sala de aula', variable=search_var, value='c')
rb_classroom.place(x=110, y=160)
rb_coffee = Radiobutton(app, text='Espaço de café', variable=search_var, value='r')
rb_coffee.place(x=250, y=160)
search_btn = Button(app, text='Pesquisar', font='Arial 12', width=30,       # Retorna os dados da pesquisa
                    command=lambda: db_handle.search_btn_press(app, search_var, search_bar))
search_btn.place(x=40, y=190)

# Adiciona um aluno novo
Label(app, text='Nome', font='Arial 10').place(x=10, y=270)
student_name = Entry(app, font='Arial 10')
student_name.place(x=130, y=270)
Label(app, text='Sobrenome', font='Arial 10').place(x=10, y=300)
student_surname = Entry(app, font='Arial 10')
student_surname.place(x=130, y=300)
student_btn = Button(app, text='Adicionar aluno',
                     command=lambda: db_handle.insert_student(student_name, student_surname),
                     font='Arial 10', width=15)
student_btn.place(x=275, y=280)

# Adiciona um sala de aula
Label(app, text='Nome da sala', font='Arial 10').place(x=10, y=360)
classroom_name = Entry(app, font='Arial 10')
classroom_name.place(x=130, y=360)
Label(app, text='Lotação', font='Arial 10').place(x=10, y=390)
classroom_capacity = Entry(app, font='Arial 10')
classroom_capacity.place(x=130, y=390)
classroom_btn = Button(app, text='Adicionar sala',
                       command=lambda: db_handle.insert_classroom(classroom_name, classroom_capacity),
                       font='Arial 10', width=15)
classroom_btn.place(x=275, y=370)

# Adiciona espaço para café
Label(app, text='Nome do espaço 1', font='Arial 10').place(x=10, y=460)
coffee_room1_name = Entry(app, font='Arial 10')
coffee_room1_name.place(x=130, y=460)
Label(app, text='Nome do espaço 2', font='Arial 10').place(x=10, y=490)
coffee_room2_name = Entry(app, font='Arial 10')
coffee_room2_name.place(x=130, y=490)
coffee_room_btn = Button(app, text='Adicionar espaço',
                         command=lambda: db_handle.insert_coffee_room(coffee_room1_name, coffee_room2_name),
                         font='Arial 10', width=15)
coffee_room_btn.place(x=275, y=470)

app.mainloop()
