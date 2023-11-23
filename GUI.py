from tkinter import *

# """Classe que define a interface gráfica da aplicação"""
class Gui():
    # Criando Janela...
    window = Tk()
    window.wm_title('Cadastro de Alunos')

    #Criando variáveis que armazenarão o texto inserido pelo usuário...
    txtName = StringVar()
    txtLastname = StringVar()
    txtCourse = StringVar()
    txtRegistration = StringVar()

    #Criando os objetos que estarão na janela...
    lblname = Label(window, text = "Nome")
    lbllastname = Label(window, text = "Sobrenome")
    lblcourse = Label (window, text = "curso")
    lblregistration = Label(window, text = "Status da Matricula")

    # Definir os campos de input (entry):
    entName = Entry(window, textvariable = txtName)
    entLastname = Entry(window, textvariable = txtLastname)
    entCourse = Entry(window, textvariable = txtCourse)
    entRegistration = Entry(window, textvariable = txtRegistration)

    #  ListBox que listará todos os clientes cadastrados.
    listStudents = Listbox(window, width=50)
    scrollStudents = Scrollbar(window)

    # Criar os botões que estarão disponíveis na interface.
    btnViewAll = Button(window, text = "Ver Alunos")
    btnSearch = Button(window, text = "Buscar por Aluno")
    btnInsert = Button(window, text = "Cadastrar Aluno")
    btnUpdate = Button(window, text = "Atualizar Aluno Selecionado")
    btnDel = Button(window, text = "Deletar Aluno Selecionado")
    btnClose = Button(window, text = "Fechar")

    #Associando os objetos ao grid da janela.
    lblname.grid(row=0, column=0)
    lbllastname.grid(row=1, column=0)
    lblcourse.grid(row=2, column=0)
    lblregistration.grid(row=3, column=0)
    entName.grid(row=0, column=1, padx=50, pady=50)
    entLastname.grid(row=1, column=1)
    entCourse.grid(row=2, column=1)
    entRegistration.grid(row=3, column=1)
    listStudents.grid(row=0, column=2, rowspan=10)
    scrollStudents.grid(row=0, column=6, rowspan=10)
    btnViewAll.grid(row=4, column=0, columnspan=2)
    btnSearch.grid(row=5, column=0, columnspan=2)
    btnInsert.grid(row=6, column=0, columnspan=2)
    btnUpdate.grid(row=7, column=0, columnspan=2)
    btnDel.grid(row=8, column=0, columnspan=2)
    btnClose.grid(row=9, column=0, columnspan=2)

    #Associando a Scrollbar com a Listbox...
    listStudents.configure(yscrollcommand=scrollStudents.set)
    scrollStudents.configure(command=listStudents.yview)

    # Variáveis para definir o padding e a largura dos elementos de input (entry).
    x_pad = 5
    y_pad = 3
    width_entry = 30

    #Adicionando um pouco de SWAG a interface...
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
        
    def run(self):
        Gui.window.mainloop()