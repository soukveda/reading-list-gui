import sqlite3

class Database:

    """
    Create a connection to our db
    """
    def __init__(self, db):
        # Connect to 'db'
        self.conn=sqlite3.connect(db)

        # Create a self variable 'cur'
        self.cur=self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, status INTEGER)")
        self.conn.commit()

    """
    Insert data into our db
    """
    def insert(self, title, author, year, status):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,status))
        self.conn.commit()


    """
    View data in our db
    """
    def view(self):
        self.cur.execute("SELECT * FROM book")
        
        rows=self.cur.fetchall()
        return rows

    """
    Search for specified data within our db
    """
    def search(self, title="", author="", year="", status=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR status=?", (title,author,year,status))
        
        rows=self.cur.fetchall()

        return rows    

    """
    Delete data in our db
    """
    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    """
    Update data in our db
    """ 
    def update(self, id, title, author, year, status):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, status=? WHERE id=?", (title,author,year,status,id))
        self.conn.commit()   

    """
    Deleting instance of Database object and closing connection to db
    """ 
    def __del__(self):
        self.conn.close()

