from tkinter import *
from tkinter import messagebox
import logging

logging.basicConfig(level=logging.DEBUG)

def add_expense():
    add_root=Tk()
    add_root.geometry("500x600+100+100")
    add_root.config(background="#da8948")
    hadding=Label(add_root,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)

    add_root.mainloop()
    logging.debug("add expense func started")
def view_expense():
    logging.debug("view expense func started")
def expense_chart():
    logging.debug("expense chart func started")



mainwindow=Tk()
mainwindow.title("expense tracker")
mainwindow.geometry("500x600+100+100")
mainwindow.config(background="#da8948")

hadding=Label(mainwindow,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)
btn1=Button(mainwindow,text="add expense",width=10,height=2,bg="gray",fg="white",border=4,command=add_expense).place(x=220,y=150)
btn2=Button(mainwindow,text="view expense",width=10,height=2,bg="gray",fg="white",border=4,command=view_expense).place(x=220,y=250)
btn3=Button(mainwindow,text="expense chart",width=10,height=2,bg="gray",fg="white",border=4,command=expense_chart).place(x=220,y=350)
mainwindow.mainloop()