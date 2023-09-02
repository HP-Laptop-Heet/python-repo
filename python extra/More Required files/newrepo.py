from tkinter import *
import subprocess as sub

root = Tk()
root.geometry("280x200")

def printvalue():
    p=pv.get()
    n=nv.get()
    print("path : "+p)
    print("name : "+n)
    #command=sub.call(["file_name"],shell=True)

Label(root,
text="Create New Repo",
font="arial 15 bold",
anchor="center").grid(row=1,column=2,pady=10)

path = Label(root, text="Path",font="arial 10 bold").grid(row=2,column=1,padx=10,pady=5)
name = Label(root, text="Name",font="arial 10 bold").grid(row=3,column=1,padx=10,pady=5)

pv=StringVar()
nv= StringVar()

pentry = Entry(root, textvariable = pv).grid(row=2,column=2)
nentry = Entry(root, textvariable = nv).grid(row=3,column=2)

Button(text="Create",
font="arial 10 bold",
bg="#a8dadc",
command= printvalue
).grid(row=5,column=2,pady=20,ipadx=5)

root.mainloop()