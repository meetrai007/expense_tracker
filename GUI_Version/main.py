from tkinter import *
from tkinter import messagebox, ttk
import logging,datetime,json


"""this code for read data from file"""
try:
    with open("expensedata.json", "r") as file:
        expense_data = json.load(file)
        list_data=list(expense_data.keys())
except:
    expense_data = {}

#this code to sore date with expense 
current_date = str(datetime.date.today())



# setting the config level here
logging.basicConfig(level=logging.DEBUG)


"""function to add expense"""
def add_expense(amount,category,decription):
    
    logging.debug("add expense function start")
    date=current_date
    if category not in expense_data:
        expense_data[category] = []
    expense_data[category].append({"date": date, "description": decription, "price": amount})
                
    with open("expensedata.json", "w") as file:
        json.dump(expense_data, file)
    logging.debug("add expense function end")




"""this function for open a different root to add expense in existing category"""
def addexpense_only():
    logging.debug("addexpense_only started")
    
    def submit_expense():
        try:
            category=combo.get()
            amount = int(entry_amount.get())
            description = entry_decription.get()
            add_expense(amount, category, description)
            messagebox.showinfo("Success", "Expense added successfully")
        except:
            
            messagebox.showwarning("invalid data", "data not added an error oucer")

        
        aeo_root.destroy()

    aeo_root=Tk()
    aeo_root.geometry("500x600+100+100")
    aeo_root.config(background="#ddd1d3")
    hadding=Label(aeo_root,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)

    lb_new_category=Label(aeo_root,text="choose a category or enter new category here")
    lb_new_category.pack()
    combo = ttk.Combobox(aeo_root,state="normal",values=list_data)
    combo.pack()
    lb_amount=Label(aeo_root,text="enter amount here")
    lb_amount.pack()
    entry_amount=Entry(aeo_root)
    entry_amount.pack()
    lb_decription=Label(aeo_root,text="enter short decription here")
    lb_decription.pack()
    entry_decription=Entry(aeo_root)
    entry_decription.pack()

    
    btn2=Button(aeo_root,text="click to add",width=20,height=2,fg="white",bg="#436af2",font="bold",command=submit_expense).place(x=140,y=450)
 
    aeo_root.mainloop()

    
"""this function for view expenses history"""
def view_expense_root():
    logging.debug("view expense func started")

"""this function for view bar graph and pie chart"""
def expense_chart_root():
    logging.debug("expense chart func started")



mainwindow=Tk()
mainwindow.title("expense tracker")
mainwindow.geometry("500x600+100+100")
mainwindow.config(background="#ddd1d3")

hadding=Label(mainwindow,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)
btn1=Button(mainwindow,text="add expense",width=20,height=2,fg="white",bg="#436af2",font="bold",command=addexpense_only).place(x=150,y=150)
btn2=Button(mainwindow,text="view expense",width=20,height=2,fg="white",bg="#436af2",font="bold",command=view_expense_root).place(x=150,y=250)
btn3=Button(mainwindow,text="expense chart",width=20,height=2,fg="white",bg="#436af2",font="bold",command=expense_chart_root).place(x=150,y=350)
mainwindow.mainloop()