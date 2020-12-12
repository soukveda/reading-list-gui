from tkinter import *
from backend import Database


# Creating a Database object
database=Database("books.db")

"""
Calling database.view() function
"""
def view_command():
    # Clear any data from the listbox (if any)
    list1.delete(0,END)

    # View all data
    for row in database.view():
        list1.insert(END,row)

"""
Calling database.search(title,author,year,isbn) function
"""
def search_command():
    list1.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), stat_text.get()):
        list1.insert(END, row)

"""
Calling database.insert() function
"""
def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), stat_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), stat_text.get()))

"""
Retrieve the selected row (tuple)
"""
def get_selected_row(event):
    global selected_tuple

    try:
        # store the index of the selected row
        index=list1.curselection()[0]

        # Store the value of the row, given it's index
        selected_tuple=list1.get(index)
        
        # Insert values of selected tuple within the entry widgets
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])

        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])

        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

"""
Delete selected row
"""
def delete_command():
    database.delete(selected_tuple[0])
    view_command()

"""
Update selected row
"""
def update_command():
    # update our database with the selected index and entry widget values
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), stat_text.get())
    view_command()

# Instantiate our window
window=Tk()

# Give our GUI a title
window.wm_title("Christopher's Reading List")

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
title_text=StringVar()
author_text=StringVar()
year_text=StringVar()
stat_text=StringVar()

# Create our entry widgets
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

e3=Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

e4=Entry(window, textvariable=stat_text)
e4.grid(row=1, column=3)

# Create a listbox
list1=Listbox(window, height=6, width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

# Create a scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# Configuring vertical scroll bar and attaching to listbox
list1.configure(yscrollcommand=sb1.set)
# Configuring scroll bar to change vertical view of listbox
sb1.configure(command=list1.yview)

# Binding list1 to a listbox event
list1.bind('<<ListboxSelect>>', get_selected_row)

# Create buttons
b1=Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()