from tkinter import *

root = Tk()
root.geometry("400x300")

Label(root,
text="Sign Up",
font="arial 15 bold",
anchor="center").grid(row=1,column=3,pady=10)

uname = Label(root, text="UserName",font="arial 10 bold").grid(row=2,column=2,padx=10,pady=5)
email = Label(root, text="Email",font="arial 10 bold").grid(row=3,column=2,padx=10,pady=5)
password = Label(root, text="Password",font="arial 10 bold").grid(row=4,column=2,padx=10,pady=5)
cpassword = Label(root, text="Confirm Password",font="arial 10 bold").grid(row=5,column=2,padx=10,pady=5)

uv= StringVar
ev= StringVar
pv= StringVar
cpv= StringVar

uentry = Entry(root, textvariable = uv).grid(row=2,column=3)
eentry = Entry(root, textvariable = ev).grid(row=3,column=3)
pentry = Entry(root, textvariable = pv).grid(row=4,column=3)
cpentry = Entry(root, textvariable = cpv).grid(row=5,column=3)


Button(text="Sign Up").grid(row=6,column=3,pady=20)

root.mainloop()