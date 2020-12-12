from tkinter import *
from database import Database

class Interface(Database):
    """This class with provide the frontend functionality of our GUI interface"""
    
    """
    Constructor class to create the Database object
    """
    def __init__(self, db):
        # Open connection to database
        Database.__init__(self, "books.db")

        # Create a window object
        self.window = window 
        
        # Give our GUI a title
        self.window.wm_title("Christopher's Reading List")

        # Create our label widgets
        lb1=Label(window, text="Title")
        lb1.grid(row=0, column=0)

        lb1=Label(window, text="Author")
        lb1.grid(row=0, column=2)

        lb1=Label(window, text="Year")
        lb1.grid(row=1, column=0)

        lb1=Label(window, text="Status")
        lb1.grid(row=1, column=2)

        # Create entry text datatype
        self.title_text=StringVar()
        self.author_text=StringVar()
        self.year_text=StringVar()
        self.stat_text=StringVar()

        # Create our entry widgets
        self.e1=Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.e2=Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.e3=Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.e4=Entry(window, textvariable=self.stat_text)
        self.e4.grid(row=1, column=3)

        # Create a listbox
        self.list1=Listbox(window, height=6, width=35)
        self.list1.grid(row=2,column=0, rowspan=6, columnspan=2)

        # Create a scrollbar
        sb1=Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        # Configuring vertical scroll bar and attaching to listbox
        self.list1.configure(yscrollcommand=sb1.set)
        # Configuring scroll bar to change vertical view of listbox
        sb1.configure(command=self.list1.yview)

        # Binding list1 to a listbox event
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # Create buttons
        b1=Button(window, text="View all", width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2=Button(window, text="Search entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3=Button(window, text="Add entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4=Button(window, text="Update selected", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5=Button(window, text="Delete selected", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6=Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)

    """
    Calling database.view() function
    """
    def view_command(self):
        # Clear any data from the listbox (if any)
        self.list1.delete(0,END)

        # View all data
        for row in Database.view(self):
            self.list1.insert(END,row)

    """
    Calling database.search(title,author,year,isbn) function
    """
    def search_command(self):
        self.list1.delete(0, END)
        for row in Database.search(self, self.title_text.get(), self.author_text.get(), self.year_text.get(), self.stat_text.get()):
            self.list1.insert(END, row)

    """
    Calling database.insert() function
    """
    def add_command(self):
        Database.insert(self, self.title_text.get(), self.author_text.get(), self.year_text.get(), self.stat_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.stat_text.get()))

    """
    Retrieve the selected row (tuple)
    """
    def get_selected_row(self,event):
        global selected_tuple

        try:
            # store the index of the selected row
            index=self.list1.curselection()[0]

            # Store the value of the row, given it's index
            selected_tuple=self.list1.get(index)
            
            # Insert values of selected tuple within the entry widgets
            self.e1.delete(0,END)
            self.e1.insert(END,selected_tuple[1])

            self.e2.delete(0,END)
            self.e2.insert(END,selected_tuple[2])

            self.e3.delete(0,END)
            self.e3.insert(END,selected_tuple[3])
            
            self.e4.delete(0,END)
            self.e4.insert(END,selected_tuple[4])
        except IndexError:
            pass

    """
    Delete selected row
    """
    def delete_command(self):
        Database.delete(self, selected_tuple[0])
        self.view_command()

    """
    Update selected row
    """
    def update_command(self):
        # update our database with the selected index and entry widget values
        Database.update(self, selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.stat_text.get())
        self.view_command()

if __name__ == '__main__':
    # Instantiate our window
    window=Tk()

    # Instantiate Interface object
    Interface("books.db")

    window.mainloop()