from tkinter import *
import subprocess as sub

root = Tk()
root.geometry("400x150")

Label(root,
text="Enter File Path",
font="arial 15 bold",
anchor="center").grid(row=1,column=3,pady=10)

uv= StringVar
uentry = Entry(root, textvariable = uv,width=60).grid(row=2,column=3,padx=15)

Button(text="RUN", command=lambda: sub.call('E:\python\python extra\shell.sh')).grid(row=3,column=3,pady=20)

root.mainloop()