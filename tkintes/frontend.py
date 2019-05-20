from tkinter import *
from backend import Database
global items
window = Tk()
window.wm_title("Book Store")
window.wm_iconbitmap("E:\\risu21kb.ico")

database=Database()

def get_selectedrow(event):

    index = listbox.curselection()[0]
    items = listbox.get(index)
    print(items)
    title_var.set(items[1])
    author_var.set(items[2])
    year_var.set(items[3])
    isbn_var.set(items[4])


def delete_function():
    index = listbox.curselection()[0]
    database.delete(index)
    print(index)
    view_data()


def search_data():
    listbox.delete(0, END)
    for row in database.search(title_var.get(), author_var.get(), year_var.get(), isbn_var.get()):
        listbox.insert(END, row)


def insert():
    title = title_var.get()
    author = author_var.get()
    year = year_var.get()
    isbn = isbn_var.get()
    database.create(title, author, year, isbn)
    listbox.insert(END, (title, author, year, isbn))


def view_data():
    listbox.delete(0, END)
    for row in database.view():
        listbox.insert(END, row)


def update_selected():
    index = listbox.curselection()[0]
    items = listbox.get(index)
    database.update(items[0],title_var.get(),author_var.get(),year_var.get(),isbn_var.get())


lbl1 = Label(window, text="Title")
lbl1.grid(row=0, column=0)

lbl2 = Label(window, text="Author")
lbl2.grid(row=0, column=2)

lbl3 = Label(window, text="Year")
lbl3.grid(row=1, column=0)

lbl4 = Label(window, text="ISBN")
lbl4.grid(row=1, column=2)

title_var = StringVar()
e1 = Entry(window, textvariable=title_var)
e1.grid(row=0, column=1)

author_var = StringVar()
e2 = Entry(window, textvariable=author_var)
e2.grid(row=0, column=3)

year_var = StringVar()
e3 = Entry(window, textvariable=year_var)
e3.grid(row=1, column=1)

isbn_var = StringVar()
e4 = Entry(window, textvariable=isbn_var)
e4.grid(row=1, column=3)

empty = Label(window)
empty.grid(row=2, column=1)

listbox = Listbox(window, height=10, width=40)
listbox.grid(row=3, column=0, rowspan=6, columnspan=2)
listbox.bind('<<ListboxSelect>>', get_selectedrow)

scrlbr = Scrollbar(window)
scrlbr.grid(row=3, column=2, rowspan=6)
listbox.configure(yscrollcommand=scrlbr.set)
scrlbr.configure(command=listbox.yview)

b1 = Button(window, text="View All", width=12, command=view_data)
b1.grid(row=3, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_data)
b2.grid(row=4, column=3)

b3 = Button(window, text="Add Entry", width=12, command=insert)
b3.grid(row=5, column=3)

b4 = Button(window, text="Update", width=12, command=update_selected)
b4.grid(row=6, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_function)
b5.grid(row=7, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=8, column=3)

window.mainloop()
