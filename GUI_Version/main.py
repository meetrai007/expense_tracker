from tkinter import *
from tkinter import messagebox, ttk
import logging,datetime,json
import matplotlib.pyplot as plt


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
logging.basicConfig(level=logging.INFO)


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

        
        add_exp_root.destroy()

    add_exp_root=Toplevel()
    add_exp_root.geometry("500x600+100+100")
    add_exp_root.config(background="#ddd1d3")
    hadding=Label(add_exp_root,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)

    lb_new_category=Label(add_exp_root,text="choose a category or enter new category here",font="bold",bg="#d9ced0",fg="black")
    lb_new_category.pack(pady=20)
    combo = ttk.Combobox(add_exp_root,state="normal",values=list_data,width=20,height=5,font="bold")
    combo.pack()
    lb_amount=Label(add_exp_root,text="enter amount here",font="bold",bg="#d9ced0",fg="black")
    lb_amount.pack(pady=20)
    entry_amount=Entry(add_exp_root,font="bold")
    entry_amount.pack()
    lb_decription=Label(add_exp_root,text="enter short decription here",font="bold",bg="#d9ced0",fg="black")
    lb_decription.pack(pady=20)
    entry_decription=Entry(add_exp_root,font="bold")
    entry_decription.pack()

    
    btn2=Button(add_exp_root,text="click to add",width=20,height=2,fg="white",bg="#436af2",font="bold",command=submit_expense).place(x=140,y=450)
 

    
"""this function for view expenses history"""
def view_expense_root():
    
    logging.debug("view expense func started")
    def monthly_data():
        textdata=""
        for item in expense_data[combo.get()]:
            textdata+=f"date:{item["date"]}  prise:{item["price"]}  decription:{item["description"]}\n"
            logging.debug(item)
            view_label_history.config(text=textdata)
    def view_expense():
        textdata=""
        for category, items in expense_data.items():
            logging.debug(f"###{category}###")
            textdata +=f"\n##########{category}##########\n"
            for item in items:
                for k, v in item.items():
                    logging.debug(f"{k}: {v}")
                    textdata+=f"{k}: {v}  "
                logging.debug(" \n\n")
                textdata+="\n"
        view_label_history.config(text=textdata)
    view_exp_root=Toplevel()
    view_exp_root.geometry("500x600+100+100")
    view_exp_root.config(bg="#ddd1d3")
    view_exp_root.title("view expense history")
    combo = ttk.Combobox(view_exp_root,state="readonly",values=list_data,width=20,height=5,font="bold")
    combo.pack()
    view_btn=Button(view_exp_root,text="view by selected category",command=monthly_data)
    view_btn.pack()
    view_btn=Button(view_exp_root,text="view all data",command=view_expense)
    view_btn.pack()
    view_label_history=Label(view_exp_root,text="")
    view_label_history.pack()


"""this function for view bar graph and pie chart"""
def expense_chart_root():
    category_titles=list(expense_data.keys())
    category_total_list=[]
    for category in category_titles:
        sum=0
        for items in expense_data[category]:
            sum+=items["price"]
        category_total_list.append(float(sum))

    def make_autopct(values):
                def my_autopct(pct):
                    total = sum(values)
                    val = int(round(pct*total/100.0))
                    return 'total:{v:d} ({p:.1f}%)'.format(p=pct,v=val)
                return my_autopct
                    
    plt.pie(category_total_list,labels=category_titles,autopct='%1.2f%%')
    plt.show()
    
        
mainwindow=Tk()
mainwindow.title("expense tracker")
mainwindow.geometry("500x600+100+100")
mainwindow.config(background="#ddd1d3")

hadding=Label(mainwindow,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)
btn1=Button(mainwindow,text="add expense",width=20,height=2,fg="white",bg="#436af2",font="bold",command=addexpense_only).place(x=150,y=150)
btn2=Button(mainwindow,text="view expense",width=20,height=2,fg="white",bg="#436af2",font="bold",command=view_expense_root).place(x=150,y=250)
btn3=Button(mainwindow,text="expense chart",width=20,height=2,fg="white",bg="#436af2",font="bold",command=expense_chart_root).place(x=150,y=350)
mainwindow.mainloop()