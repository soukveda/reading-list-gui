import sqlite3

"""
Create a connection to our db
"""
def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, status INTEGER)")
    
    conn.commit()
    conn.close()

"""
Insert data into our db
"""
def insert(title, author, year, status):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()

    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,status))
    
    conn.commit()
    conn.close()

"""
View data in our db
"""
def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()

    cur.execute("SELECT * FROM book")
    
    rows=cur.fetchall()
    conn.close()    

    return rows

"""
Search for specified data within our db
"""
def search(title="", author="", year="", status=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()

    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR status=?", (title,author,year,status))
    
    rows=cur.fetchall()
    conn.close()    

    return rows    

"""
Delete data in our db
"""
def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()

    cur.execute("DELETE FROM book WHERE id=?", (id,))
    
    conn.commit()
    conn.close()   

"""
Update data in our db
""" 
def update(id, title, author, year, status):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()

    cur.execute("UPDATE book SET title=?, author=?, year=?, status=? WHERE id=?", (title,author,year,status,id))
    
    conn.commit()
    conn.close()    

# Create our database
connect()
