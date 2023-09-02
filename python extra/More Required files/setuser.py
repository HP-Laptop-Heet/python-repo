from tkinter import *
import subprocess as sub
import sys
import os

root = Tk()
root.geometry("280x200")

def printvalue():
    u=uv.get()
    e=ev.get()
    print("path : "+u)
    print("name : "+e)
    #command=sub.call(["file_name"],shell=True)

Label(root,
text="Set New User",
font="arial 15 bold",
anchor="center").grid(row=1,column=2,pady=10)

uname = Label(root, text="Username",font="arial 10 bold").grid(row=2,column=1,padx=10,pady=5)
email = Label(root, text="Email",font="arial 10 bold").grid(row=3,column=1,padx=10,pady=5)

uv= StringVar()
ev= StringVar()

uentry = Entry(root, textvariable = uv).grid(row=2,column=2)
eentry = Entry(root, textvariable = ev).grid(row=3,column=2)

Button(text="Set",
font="arial 10 bold",
bg="#a8dadc",
command=printvalue
).grid(row=5,column=2,pady=20,ipadx=5)

root.mainloop()