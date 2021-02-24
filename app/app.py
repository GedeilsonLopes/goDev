from tkinter import *

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
search_bar = Entry(app, width=50, font='Arial 10').place(x=10, y=130)
rb_student = Radiobutton(app, text='Aluno', value='a', variable=search_var).place(x=10, y=160)
rb_classroom = Radiobutton(app, text='Sala de aula', value='c', variable=search_var).place(x=110, y=160)
rb_coffee = Radiobutton(app, text='Espaço de café', value='r', variable=search_var).place(x=250, y=160)
search_btn = Button(app, text='Pesquisar', font='Arial 12', width=30).place(x=40, y=190)

# Adiciona um aluno novo
Label(app, text='Nome', font='Arial 12').place(x=10, y=270)
student_name_entry = Entry(app, font='Arial 10').place(x=140, y=270)
Label(app, text='Sobrenome', font='Arial 12').place(x=10, y=300)
student_surname_entry = Entry(app, font='Arial 10').place(x=140, y=300)
student_btn = Button(app, text='Adicionar aluno', font='Arial 12', width=15).place(x=290, y=280)

# Adiciona um sala de aula
Label(app, text='Nome da sala', font='Arial 12').place(x=10, y=360)
classroom_name_entry = Entry(app, font='Arial 10').place(x=140, y=360)
Label(app, text='Lotação', font='Arial 12').place(x=10, y=390)
classroom_capacity_entry = Entry(app, font='Arial 10').place(x=140, y=390)
classroom_btn = Button(app, text='Adicionar sala', font='Arial 12', width=15).place(x=290, y=370)

# Adiciona espaço para café
Label(app, text='Nome do espaço', font='Arial 12').place(x=10, y=460)
coffee_room_entry = Entry(app, font='Arial 10').place(x=140, y=460)
Label(app, text='Capacidade', font='Arial 12').place(x=10, y=490)
coffee_room_capacity_entry = Entry(app, font='Arial 10').place(x=140, y=490)
coffee_room_btn = Button(app, text='Adicionar espaço', font='Arial 12', width=15).place(x=290, y=470)

# Informações referente a pesquisa font='Arial 14'

info_frame = Label(app, text='Quadro de Informações', bg='gray')

app.mainloop()
