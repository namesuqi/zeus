# coding=utf-8
"""
TODO: Add description for file

__author__ = 'zengyuetian'

"""
from Tkinter import *
root = Tk()
root.title("Join Leifeng")
root.geometry('400x300')

Label(root, text='hehe', font=('Arial', 20)).pack()

frm = Frame(root)

frm_L = Frame(frm)
Label(frm_L, text='Hello', font=('Arial', 15)).pack(side=LEFT)
Label(frm_L, text='world', font=('Arial', 15)).pack(side=TOP)
frm_L.pack(side=LEFT)

#right
frm_R = Frame(frm)
Label(frm_R, text='', font=('Arial', 15)).pack(side=TOP)
Label(frm_R, text='', font=('Arial', 15)).pack(side=TOP)
frm_R.pack(side=RIGHT)

frm.pack()


# l = Label(root, text="show", bg="green", font=("Arial", 12), width=5, height=2)
# l.pack(side=LEFT)



t = Text(root)
t.pack()

root.mainloop()

root.resizable(width=False, height=True)

root.mainloop()
