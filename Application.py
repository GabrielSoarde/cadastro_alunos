from GUI import *
import Backend as core


app = None

def view_command():
    rows = core.view()
    app.listStudents.delete(0, END)
    for r in rows:
        app.listStudents.insert(END, r)

def search_command():
    app.listStudents.delete(0, END)
    rows = core.search(app.txtName.get(), app.txtLastname.get(), app.txtCourse.get(), app.txtRegistration.get())
    for r in rows:
        app.listStudents.insert(END, r)

def insert_command():
    core.insert(app.txtName.get(), app.txtLastname.get(), app.txtCourse.get(), app.txtRegistration.get())
    view_command()

def update_command():
    core.update(selected[0],app.txtName.get(),app.txtLastname.get(),app.txtCourse.get(), app.txtRegistration.get())
    view_command()

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()


def getSelectedRow(event):
    global selected
    index = app.listStudents.curselection()[0]
    selected = app.listStudents.get(index)
    app.entName.delete(0, END)
    app.entName.insert(END, selected[1])
    app.entLastname.delete(0, END)
    app.entLastname.insert(END, selected[2])
    app.entCourse.delete(0, END)
    app.entCourse.insert(END, selected[3])
    app.entRegistration.delete(0, END)
    app.entRegistration.insert(END, selected[4])
    return selected


if __name__ == "__main__":
    app = Gui()
    app.listStudents.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnSearch.configure(command=search_command)
    app.btnInsert.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()