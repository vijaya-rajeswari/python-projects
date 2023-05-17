from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():

    screen =Tk()
    screen.geometry("375x398")


#icon
# image_icon = PhotoImage(file="key.png")
# screen.iconphoto(False,image_icon)
    screen.title("pctApp")
    Label(text="enter text for encryption and decryption",fg="black",font=("calbri",13)).place(x=10,y=10)
    text1=Text(font="robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)


    Label(text="enter secret key for  encryption and decryption",fg="black",font=("calibra",13)).place(x=10,y=200)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25)).place(x=10,y=100)


    screen.mainloop()


main_screen()
