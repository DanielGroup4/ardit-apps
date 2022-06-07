from tkinter import *
from backend import DataBase

database = DataBase("cheatsheets.db")

window = Tk()


class Window(object):

    def __init__(self, window):
        self.window = window
        self.window.wm_title("App cheatsheets") # title app

        l1 = Label(window, text= "Cheatsheet")
        l1.grid(row= 0, column= 0)

        l2 = Label(window, text= "Tema")
        l2.grid(row= 0, column= 2)

        l3 = Label(window, text= "Fecha")
        l3.grid(row= 1, column= 0)

        l4 = Label(window, text= "ID_cheat")
        l4.grid(row= 1, column= 2)

        self.cheatsheet_text = StringVar() 
        self.e1 = Entry(window, textvariable= self.cheatsheet_text)
        self.e1.grid(row= 0, column= 1)

        self.tema_text = StringVar()
        self.e2 = Entry(window, textvariable= self.tema_text)
        self.e2.grid(row= 0, column= 3)

        self.fecha_text = StringVar()
        self.e3 = Entry(window, textvariable= self.fecha_text)
        self.e3.grid(row= 1, column= 1)

        self.id_cheat = StringVar()
        self.e4 = Entry(window, textvariable= self.id_cheat)
        self.e4.grid(row= 1, column= 3)

        self.list1 = Listbox(window, height= 6, width= 35)
        self.list1.grid(row= 2, column= 0, rowspan= 6, columnspan= 2)

        sb1 = Scrollbar(window)
        sb1.grid(row= 2, column= 2, rowspan= 6)

        self.list1.configure(yscrollcommand= sb1.set)
        sb1.configure(command= self.list1.yview)

        self.list1.bind("<<ListboxSelect>>", self.get_selected_row)

        b1 = Button(window, text= "View all", width= 12, command= self.view_command)
        b1.grid(row= 2, column= 3)

        b2 = Button(window, text= "Search entry", width= 12, command= self.search_command)
        b2.grid(row= 3, column= 3)

        b3 = Button(window, text= "Add entry", width= 12, command= self.add_command)
        b3.grid(row= 4, column= 3)

        b4 = Button(window, text= "Update selected", width= 12, command= self.update_command)
        b4.grid(row= 5, column= 3)

        b5 = Button(window, text= "Delete selected", width= 12, command= self.delete_command)
        b5.grid(row= 6, column= 3)

        b6 = Button(window, text= "Close", width= 12, command= window.destroy)
        b6.grid(row= 7, column= 3)


    def get_selected_row(self, event):
        try:
            #global selected_tuple
            index = self.list1.curselection()[0] # indice de la lista comienza desde 0
            #print(index)
            self.selected_tuple = self.list1.get(index) # obtener la tupla segun el indice
            #print(selected_tuple[0]) 
            self.e1.delete(0, END)
            self.e1.insert(END, self.selected_tuple[1]) # inserta valores en cada campo
            self.e2.delete(0, END)
            self.e2.insert(END, self.selected_tuple[2]) # inserta valores en cada campo
            self.e3.delete(0, END)
            self.e3.insert(END, self.selected_tuple[3]) # inserta valores en cada campo
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_tuple[4]) # inserta valores en cada campo
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row) 

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.cheatsheet_text.get(), self.tema_text.get(), self.fecha_text.get(), self.id_cheat.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.cheatsheet_text.get(), self.tema_text.get(), self.fecha_text.get(), self.id_cheat.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.cheatsheet_text.get(), self.tema_text.get(), self.fecha_text.get(), self.id_cheat.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])

    def update_command(self):
        database.update(self.selected_tuple[0], self.cheatsheet_text.get(), self.tema_text.get(), self.fecha_text.get(), self.id_cheat.get())

Window(window)
window.mainloop()
