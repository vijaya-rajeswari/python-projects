from tkinter import *

root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

Label(root, text="Register Form", font="ar 15 bold").grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmood = Label(root, text="Payment Mood")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmoodvalue = StringVar()

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmoodentry = Entry(root, textvariable=paymentmoodvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)

checkvalue = IntVar()

# creating checkbox
checkbtn = Checkbutton(root, text="Remember me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

# submit button
Button(root, text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()














# from tkinter import *
# import sqlite3
#
# root = Tk()
# root.geometry("500x300")
#
# def getvals():
#     # Establish a connection to the database
#     conn = sqlite3.connect("registration.db")
#
#     # Create a cursor object to execute SQL queries
#     cursor = conn.cursor()
#
#     # Create a table if it doesn't exist
#     cursor.execute('''CREATE TABLE IF NOT EXISTS registrations
#                       (name TEXT, phone TEXT, gender TEXT, emergency TEXT, paymentmood TEXT)''')
#
#     # Insert the form data into the table
#     cursor.execute("INSERT INTO registrations VALUES (?, ?, ?, ?, ?)",
#                    (namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmoodvalue.get()))
#
#     # Commit the transaction
#     conn.commit()
#
#     # Close the database connection
#     conn.close()
#
#     print("Data inserted successfully!")
#
# Label(root, text="Register Form", font="ar 15 bold").grid(row=0, column=3)
#
# name = Label(root, text="Name")
# phone = Label(root, text="Phone")
# gender = Label(root, text="Gender")
# emergency = Label(root, text="Emergency")
# paymentmood = Label(root, text="Payment Mood")
#
# name.grid(row=1, column=2)
# phone.grid(row=2, column=2)
# gender.grid(row=3, column=2)
# emergency.grid(row=4, column=2)
# paymentmood.grid(row=5, column=2)
#
# namevalue = StringVar()
# phonevalue = StringVar()
# gendervalue = StringVar()
# emergencyvalue = StringVar()
# paymentmoodvalue = StringVar()
#
# nameentry = Entry(root, textvariable=namevalue)
# phoneentry = Entry(root, textvariable=phonevalue)
# genderentry = Entry(root, textvariable=gendervalue)
# emergencyentry = Entry(root, textvariable=emergencyvalue)
# paymentmoodentry = Entry(root, textvariable=paymentmoodvalue)
#
# nameentry.grid(row=1, column=3)
# phoneentry.grid(row=2, column=3)
# genderentry.grid(row=3, column=3)
# emergencyentry.grid(row=4, column=3)
# paymentmoodentry.grid(row=5, column=3)
#
# checkvalue = IntVar()
#
# # creating checkbox
# checkbtn = Checkbutton(root, text="Remember me?", variable=checkvalue)
# checkbtn.grid(row=6, column=3)
#
# # submit button
# Button(root, text="Submit", command=getvals).grid(row=7, column=3)
#
# root.mainloop()
