from tkinter import *
from tkinter import messagebox
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
    print(amount,category,decription)
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
            selected_categories = [listbox.get(i) for i in listbox.curselection()]
            amount = int(entry_amount.get())
            description = entry_decription.get()

            for category in selected_categories:
                add_expense(amount, category, description)
            messagebox.showinfo("Success", "Expense added successfully in old category")
        except:
            amount = int(entry_amount.get())
            description = entry_decription.get()
            new_category=entry_new_category.get()
            add_expense(amount, new_category, description)
            messagebox.showinfo("Success", "Expense added successfully in new category")

        
        aeo_root.destroy()

    aeo_root=Tk()
    aeo_root.geometry("500x600+100+100")
    aeo_root.config(background="#ddd1d3")
    hadding=Label(aeo_root,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)

    listbox=Listbox(aeo_root,selectmode=MULTIPLE,height=10)
    listbox.pack()
    for item in list_data: 
        listbox.insert(END, item)
    lb_new_category=Label(aeo_root,text="enter new category here").pack()
    entry_new_category=Entry(aeo_root)
    entry_new_category.pack()
    lb_amount=Label(aeo_root,text="enter amount here").pack()
    entry_amount=Entry(aeo_root)
    entry_amount.pack()
    lb_decription=Label(aeo_root,text="enter short decription here").pack()
    entry_decription=Entry(aeo_root)
    entry_decription.pack()

    
    btn2=Button(aeo_root,text="click to add",width=20,height=2,fg="white",bg="#436af2",font="bold",command=submit_expense).place(x=140,y=350)
 
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