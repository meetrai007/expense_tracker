from tkinter import Toplevel, Label, Button, ttk
from tkinter import StringVar
import logging
from datetime import datetime

# Dummy expense data for demonstration
expense_data = {
    'Food': [{'date': '2024-09-01', 'price': '10', 'description': 'Lunch'},
             {'date': '2024-09-02', 'price': '20', 'description': 'Dinner'}],
    'Transport': [{'date': '2024-09-01', 'price': '15', 'description': 'Bus fare'},
                  {'date': '2024-09-03', 'price': '25', 'description': 'Taxi'}]
}

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
            start_date_obj = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date_obj = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            view_label_history.config(text="Invalid date format. Please use YYYY-MM-DD.")
            return
        
        textdata = ""
        for category, items in expense_data.items():
            textdata += f"\n##########{category}##########\n"
            for item in items:
                item_date_obj = datetime.strptime(item['date'], '%Y-%m-%d')
                if start_date_obj <= item_date_obj <= end_date_obj:
                    textdata += f"date: {item['date']}  price: {item['price']}  description: {item['description']}\n"
        view_label_history.config(text=textdata)

    view_exp_root = Toplevel()
    view_exp_root.geometry("600x700+100+100")
    view_exp_root.config(bg="#ddd1d3")
    view_exp_root.title("View Expense History")

    combo = ttk.Combobox(view_exp_root, state="readonly", values=list_data, width=20, height=5, font="bold")
    combo.pack()

    view_btn_category = Button(view_exp_root, text="View by Selected Category", command=single_category_data)
    view_btn_category.pack()

    view_btn_all = Button(view_exp_root, text="View All Data", command=view_expense)
    view_btn_all.pack()

    view_btn_date = Button(view_exp_root, text="View by Date Range", command=view_expense_by_date)
    view_btn_date.pack()

    start_date = StringVar()
    end_date = StringVar()
    
    Label(view_exp_root, text="Start Date (YYYY-MM-DD):").pack()
    start_date_entry = ttk.Entry(view_exp_root, textvariable=start_date)
    start_date_entry.pack()

    Label(view_exp_root, text="End Date (YYYY-MM-DD):").pack()
    end_date_entry = ttk.Entry(view_exp_root, textvariable=end_date)
    end_date_entry.pack()

    view_label_history = Label(view_exp_root, text="")
    view_label_history.pack()

# Assuming that you have set up your logging configuration somewhere in your code.
logging.basicConfig(level=logging.DEBUG)
