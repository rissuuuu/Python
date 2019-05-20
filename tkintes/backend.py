import sqlite3

class Database:
    def __init__(self):
        con=sqlite3.connect("E:\\sqlite.db")
        cur=con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
        con.commit()
        con.close()

    def create(self,title,author,year,isbn):
        con = sqlite3.connect("E:\\sqlite.db")
        cur = con.cursor()
        cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        con.commit()
        con.close()


    def view(self):
        con = sqlite3.connect("E:\\sqlite.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM book")
        row=cur.fetchall()
        con.commit()
        con.close()
        return row


    def search(self,title="",author="",year="",isbn=""):
        con = sqlite3.connect("E:\\sqlite.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        con.commit()
        row=cur.fetchall()
        con.close()
        return row

    def delete(self,id):
        con = sqlite3.connect("E:\\sqlite.db")
        cur = con.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        con.commit()
        row = cur.fetchall()
        con.close()
        return row

    def update(self,id,title,author,year,isbn):
        con = sqlite3.connect("E:\\sqlite.db")
        cur = con.cursor()
        cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
        con.commit()
        row = cur.fetchall()
        con.close()
        return row
