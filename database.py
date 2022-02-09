from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Using SQLite3 database")
root.iconbitmap("pictures/mask_icon.ico")
root.geometry("400x600")

# Database
# Create a database or connect to one
conn = sqlite3.connect("address_book.db")

# Create cursor
c = conn.cursor()


# Create table
# c.execute(""" CREATE TABLE addresses (
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     state text,
#     zipcode integer
#     )
# """)

# Create Submit function
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            "f_name": f_name.get(),
            "l_name": l_name.get(),
            "address": address.get(),
            "city": city.get(),
            "state": state.get(),
            "zipcode": zipcode.get()
        }
    )

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    # Clear Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT *, oid FROM addresses")
    query_results = c.fetchall()
    print(query_results)

    print_records = ""
    for record in query_results:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=20, column=0, columnspan=2)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()    


# Delete a record       
def delete():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE FROM addresses WHERE oid = " + select_id.get())

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()    

    select_id.delete(0, END)


# Update record
def edit():

    # Create global variables
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor    
    global editor
    
    editor = Tk()
    editor.title("Edit Address Record")
    editor.iconbitmap("pictures/mask_icon.ico")
    editor.geometry("400x600")

    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    record_id = select_id.get()
    # Query the Database
    c.execute("SELECT * FROM addresses WHERE oid = " + str(record_id))
    query_results = c.fetchall()
    print(query_results)


    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # Create Text Box Labels
    f_name_label_editor =  Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10, 0))

    l_name_label_editor =  Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0)

    address_label_editor =  Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0)

    city_label_editor =  Label(editor, text="City")
    city_label_editor.grid(row=3, column=0)

    state_label_editor =  Label(editor, text="State")
    state_label_editor.grid(row=4, column=0)

    zipcode_label_editor =  Label(editor, text="Zipcode")
    zipcode_label_editor.grid(row=5, column=0)


    # Create Submit Button
    save_btn_editor  = Button(editor, text="Save Changes", command=save)
    save_btn_editor.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=100, ipady=10)

    for record in query_results:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
        

# Editor Save Button
def save():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create cursor
    c = conn.cursor()

    record_id = select_id.get()

    # Insert into table
    c.execute("""UPDATE addresses SET 
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        WHERE oid = :oid""",
        {
            "first": f_name_editor.get(),
            "last": l_name_editor.get(),
            "address": address_editor.get(),
            "city": city_editor.get(),
            "state": state_editor.get(),
            "zipcode": zipcode_editor.get(),
            "oid": record_id
        }
    )

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    editor.destroy()


# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

select_id = Entry(root, width=5)
select_id.grid(row=8, column=1)

# Create Text Box Labels
f_name_label =  Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label =  Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label =  Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label =  Label(root, text="City")
city_label.grid(row=3, column=0)

state_label =  Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label =  Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

select_id_label = Label(root, text="Select ID")
select_id_label.grid(row=8, column=0)


# Create Submit Button
submit_btn  = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=100, ipady=10)

# Create Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=12, column=0, columnspan=2, padx=10, pady=10, ipadx=50, ipady=10)

# Create Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=14, column=0, columnspan=2, padx=10, pady=10, ipadx=50, ipady=10)

# Create Edit Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=16, column=0, columnspan=2, padx=10, pady=10, ipadx=50, ipady=10)


# Commit changes
conn.commit()

# Close connection
conn.close()



root.mainloop()
