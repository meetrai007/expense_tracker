from tkinter import *
from tkinter import messagebox
import logging

logging.basicConfig(level=logging.DEBUG)

def addexpense_only():
    logging.debug("addexpense_only started")

    apo_root=Tk()
    apo_root.geometry("500x600+100+100")
    apo_root.config(background="#da8948")
    hadding=Label(apo_root,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)

    btn2=Button(apo_root,text="click to add",width=30,height=2,bg="gray",fg="white",border=4).place(x=150,y=250)
 

    apo_root.mainloop()

def addexpense_category():
    logging.debug("addexpense_category started")

    aeac_root=Tk()
    aeac_root.geometry("500x600+100+100")
    aeac_root.config(background="#da8948")
    hadding=Label(aeac_root,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)
    lb_amount=Label(aeac_root,text="enter amount").pack()
    entry_amount=Entry(aeac_root).pack()
    lb_category=Label(aeac_root,text="enter category").pack()
    entry_category=Entry(aeac_root).pack()
    lb_decription=Label(aeac_root,text="enter short decription").pack()
    entry_decription=Entry(aeac_root).pack()
    btn2=Button(aeac_root,text="click to add",width=30,height=2,bg="gray",fg="white",border=4).place(x=150,y=250)
 

    aeac_root.mainloop()


def add_expense_root():
    add_root=Tk()
    add_root.geometry("500x600+100+100")
    add_root.config(background="#da8948")
    hadding=Label(add_root,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)
    btn1=Button(add_root,text="add expense in exesting category",width=30,height=2,bg="gray",fg="white",border=4,command=addexpense_only).place(x=150,y=150)
    btn2=Button(add_root,text="add expense in new category",width=30,height=2,bg="gray",fg="white",border=4,command=addexpense_category).place(x=150,y=250)
 

    add_root.mainloop()
    logging.debug("add expense func started")
    
def view_expense_root():
    logging.debug("view expense func started")
def expense_chart_root():
    logging.debug("expense chart func started")



mainwindow=Tk()
mainwindow.title("expense tracker")
mainwindow.geometry("500x600+100+100")
mainwindow.config(background="#da8948")

hadding=Label(mainwindow,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)
btn1=Button(mainwindow,text="add expense",width=10,height=2,bg="gray",fg="white",border=4,command=add_expense_root).place(x=220,y=150)
btn2=Button(mainwindow,text="view expense",width=10,height=2,bg="gray",fg="white",border=4,command=view_expense_root).place(x=220,y=250)
btn3=Button(mainwindow,text="expense chart",width=10,height=2,bg="gray",fg="white",border=4,command=expense_chart_root).place(x=220,y=350)
mainwindow.mainloop()