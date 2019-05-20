import sqlite3


def create_table():
    con=sqlite3.connect("E:\\sqlite.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item Text,quantity INTEGER,price REAL)")
    con.commit()
    con.close()


def insert_item(item,quantity,price):
    con=sqlite3.connect("E:\\sqlite.db")
    cur=con.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    con.commit()
    con.close()


def view_database():
    con = sqlite3.connect("E:\\sqlite.db")
    cur = con.cursor()
    cur.execute("SELECT * from store")
    rows=cur.fetchall()
    con.commit()
    con.close()
    return rows

def delete_date(item):
    con = sqlite3.connect("E:\\sqlite.db")
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    con.commit()
    con.close()


def update(quantity,price,item):
    con = sqlite3.connect("E:\\sqlite.db")
    cur = con.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item))
    con.commit()
    con.close()


print(view_database(),end="\n")
#create_table()
item=input("Enter item")
qtt=int(input("Enter quantity"))
price=int(input("Enter price"))
#insert_item(item,qtt,price)

#delete_date(qtt)
update(qtt,price,item)
print(view_database(),end="\n")