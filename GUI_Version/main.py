from tkinter import *
from tkinter import messagebox, ttk
import logging,datetime,json
import matplotlib.pyplot as plt
from tkcalendar import Calendar, DateEntry


"""this code for read data from file"""
try:
    with open("expensedata.json", "r") as file:
        expense_data = json.load(file)
        list_data=list(expense_data.keys())
except:
    expense_data = {}

#this code to sore date with expense 
current_date = str(datetime.date.today())

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return 'total:{v:d} ({p:.1f}%)'.format(p=pct,v=val)
    return my_autopct

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
 

list_data = list(expense_data.keys())  # List of categories for the combobox

def view_expense_root():
    logging.debug("view expense func started")

    def single_category_data():
        textdata = ""
        for item in expense_data[combo.get()]:
            textdata += f"date: {item['date']}  price: {item['price']}  description: {item['description']}\n"
            logging.debug(item)
        view_label_history.config(text=textdata)
    
    def view_expense():
        textdata = ""
        for category, items in expense_data.items():
            logging.debug(f"###{category}###")
            textdata += f"\n##########{category}##########\n"
            for item in items:
                for k, v in item.items():
                    logging.debug(f"{k}: {v}")
                    textdata += f"{k}: {v}  "
                logging.debug(" \n\n")
                textdata += "\n"
        view_label_history.config(text=textdata)

    def view_expense_by_date():
        start_date_str = start_date.get()
        end_date_str = end_date.get()
        try:
            start_date_obj = datetime.datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date_obj = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            view_label_history.config(text="Invalid date format. Please use YYYY-MM-DD.")
            return
        
        textdata = ""
        for category, items in expense_data.items():
            textdata += f"\n##########{category}##########\n"
            for item in items:
                item_date_obj = datetime.datetime.strptime(item['date'], '%Y-%m-%d')
                if start_date_obj <= item_date_obj <= end_date_obj:
                    textdata += f"date: {item['date']}  price: {item['price']}  description: {item['description']}\n"
        view_label_history.config(textvariable=textdata)

    view_exp_root = Toplevel()
    view_exp_root.geometry("500x600+100+100")
    view_exp_root.config(bg="#ddd1d3")
    view_exp_root.title("View Expense History")

    Label(view_exp_root, text="Select a category and view expense",font="bold",bg="#d9ced0",fg="black").grid(column=1,row=1,pady=20)

    combo = ttk.Combobox(view_exp_root, state="readonly", values=list_data, width=20, height=5, font="bold")
    combo.grid(row=2,column=1)

    view_btn_category = Button(view_exp_root, text="View expense",width=20,height=1,fg="white",bg="#436af2",font="bold", command=single_category_data)
    view_btn_category.grid(row=3,column=1,pady=5)

    or_=Label(view_exp_root, text="OR",bg="#ddd1d3")
    or_.grid(row=4,column=1,pady=15)

    Label(view_exp_root, text="click View All Data to view all time data",font="bold",bg="#d9ced0",fg="black").grid(row=1,column=1,pady=20)
    view_btn_all = Button(view_exp_root, text="View All Data",width=20,height=1,fg="white",bg="#436af2",font="bold", command=view_expense)
    view_btn_all.grid(row=5,column=1)

    or_=Label(view_exp_root, text="OR",bg="#ddd1d3")
    or_.grid(row=6,column=1,pady=15)


    start_date = StringVar()
    end_date = StringVar()
    
    
    Label(view_exp_root, text="Enter a time period to to search",font="bold",bg="#d9ced0",fg="black").grid(row=1,column=1,pady=20)
    Label(view_exp_root, text="Start Date (YYYY-MM-DD):",bg="#d9ced0",fg="black").grid(row=7,column=1)
    start_date_entry = ttk.Entry(view_exp_root, textvariable=start_date)
    start_date_entry.grid(row=8,column=1)

    Label(view_exp_root, text="End Date (YYYY-MM-DD):",bg="#d9ced0",fg="black").grid(row=9,column=1)
    end_date_entry = ttk.Entry(view_exp_root, textvariable=end_date)
    end_date_entry.grid(row=10,column=1)

    view_btn_date = Button(view_exp_root, text="View by Date Range",width=20,height=1,fg="white",bg="#436af2",font="bold", command=view_expense_by_date)
    view_btn_date.grid(row=11,column=1,pady=5)

    view_label_history = Entry(view_exp_root, state='readonly',bg="#ddd1d3")
    view_label_history.grid(column=2)

    # expense_view=Toplevel()
    # expense_view.geometry("+650+100")
    # expense_view.config(bg="#ddd1d3")
    # view_label_history = Label(expense_view, text="",bg="#ddd1d3")
    # view_label_history.pack()



"""this function for view bar graph and pie chart"""
def expense_chart_root():
    
    def category_pie():    
        category_titles=list(expense_data.keys())
        category_total_list=[]
        for category in category_titles:
            sum=0
            for items in expense_data[category]:
                sum+=items["price"]
            category_total_list.append(float(sum))
        plt.pie(category_total_list,labels=category_titles,autopct=make_autopct(category_total_list))
        plt.show()

    def example():
        def print_sel():
            global startdate
            startdate=cal2.selection_get()
            logging.debug(startdate)
            sdate.config(text=startdate)
        def print_sel2():
            global enddate
            enddate=cal2.selection_get()
            edate.config(text=enddate)
            logging.debug(enddate)

        top = Toplevel(mainwindow)
        top.geometry("300x400+500+100")

        cal2 = Calendar(top,
                    font="Arial 14", selectmode='day',
                    cursor="hand1", year=2024, month=8, day=31)
        cal2.pack(fill="both", expand=True)
        ttk.Button(top, text="start date", command=print_sel).pack()
        ttk.Button(top, text="end date", command=print_sel2).pack()
        # date_wise_bar(cal2.selection_get(),cal2.selection_get())

    
    def date_wise_bar():
        
        
        dayly_spent={}
        
        for categoreys in expense_data.keys():
            for list in expense_data[categoreys]:
                todaydate=datetime.datetime.strptime(list["date"], "%Y-%m-%d").date()
                if startdate<=todaydate<=enddate:
                    dayly_spent[list["date"]]=0
                    dayly_spent[list["date"]]+=list["price"]
                    
        plt.bar(dayly_spent.keys(),dayly_spent.values(),width=.2)
        plt.title("Total spend record daily")
        plt.xlabel("Dates of total spends")
        plt.ylabel("daily total spend amount")
        plt.show()

    chart_root=Toplevel()
            
    chart_root.title("expense tracker")
    chart_root.geometry("500x600+100+100")
    chart_root.config(background="#ddd1d3")
    hadding=Label(chart_root,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)
    btn1=Button(chart_root,text="category wise chart",width=20,height=2,fg="white",bg="#436af2",font="bold",command=category_pie).place(x=150,y=150)
    btn2=Button(chart_root,text="enter date here",width=20,height=2,command=example).place(x=190,y=270)
    sdate=Label(chart_root,text="start date")
    sdate.place(x=190,y=320)
    edate=Label(chart_root,text="end date")
    edate.place(x=290,y=320)

    btn3=Button(chart_root,text="view daily expense",width=20,height=2,fg="white",bg="#436af2",font="bold",command=lambda:date_wise_bar()).place(x=150,y=350)


      
    
     
mainwindow=Tk()
mainwindow.title("expense tracker")
mainwindow.geometry("500x600+100+100")
mainwindow.config(background="#ddd1d3")
hadding=Label(mainwindow,text="welcome to expense tracker app",bg="blue",fg="white",font=6,width=30).pack(fill=BOTH,ipadx=20,ipady=20)
btn1=Button(mainwindow,text="add expense",width=20,height=2,fg="white",bg="#436af2",font="bold",command=addexpense_only).place(x=150,y=150)
btn2=Button(mainwindow,text="view expense",width=20,height=2,fg="white",bg="#436af2",font="bold",command=view_expense_root).place(x=150,y=250)
btn3=Button(mainwindow,text="expense chart",width=20,height=2,fg="white",bg="#436af2",font="bold",command=expense_chart_root).place(x=150,y=350)
mainwindow.mainloop()