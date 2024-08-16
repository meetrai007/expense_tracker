import json
import datetime
import logging
import matplotlib.pyplot as plt


logging.basicConfig(level=logging.INFO)

logging.info("############## WELCOME TO EXPENSE TRACKER APPLICATION ##############")

# Load the expense data from the JSON file
try:
    with open("expensedata.json", "r") as file:
        expense_data = json.load(file)
except:
    expense_data = {}

try:
    with open("daily_spend_record.json", "r") as file2:
        daily_spend_record = json.load(file2)
except:
    daily_spend_record = {}


current_date = datetime.date.today()

while True:
    try:
        feature = int(input("""   
                                1. Add expense
                                2. Total spend in a specific category
                                3. Total spends
                                4. View all expense history
                                5. View pie chart of Total spend in categorys
                                6. View bar chart of daily spend
                                7. Exit
                                Enter what you want to do: """))
    except ValueError:
        logging.info("\n### Choose a valid option: 1, 2, 3, 4, or 5 ###\n")
        continue

    if feature == 1:
        choice = int(input("""##### Choose an option #####
                                1. Add expense in new category
                                2. Add expense in existing category
                                Enter your choice (1 or 2): """))
        if choice == 1:
            continuty = "y"
            while continuty.lower() != "n":
                try:
                    category = str(input("Enter category in which you spent: "))
                    description = str(input("Write a short description of the spend: "))
                    price = float(input("Enter the amount you spent: "))
                except ValueError:
                    logging.info("\n### Enter details carefully ###\n")
                    continue
                
                """this code for daily total spend and store in a json file"""
                if str(current_date) in daily_spend_record:
                    daily_spend_record[str(current_date)]=daily_spend_record[str(current_date)]+price
                    with open("daily_spend_record.json", "w") as file2:
                        json.dump(daily_spend_record, file2)
                if str(current_date) not in daily_spend_record:
                    daily_spend_record[str(current_date)]=price
                    with open("daily_spend_record.json", "w") as file2:
                        json.dump(daily_spend_record, file2)

                if category not in expense_data:
                    expense_data[category] = []
                expense_data[category].append({"date": str(current_date), "description": description, "price": price})
                
                with open("expensedata.json", "w") as file:
                    json.dump(expense_data, file)

                
                continuty = str(input("Enter 'y' to add more expenses or 'n' to exit (y/n): "))

        if choice == 2:
            logging.info("\n##### Choose a category #####")
            cat_list = list(expense_data.keys())
            for idx, key in enumerate(cat_list, 1):
                logging.info(f"\t{idx}. {key}")

            try:
                enter_category = int(input("Choose a category in which you want to add expense: ")) - 1
                description = str(input("Write a short description of the spend: "))
                price = float(input("Enter the amount you spent: "))
                
                expense_data[cat_list[enter_category]].append({"date": str(current_date), "description": description, "price": price})
                with open("expensedata.json", "w") as file:
                    json.dump(expense_data, file)
                
                """this code for daily total spend and store in a json file"""
                if str(current_date) in daily_spend_record:
                    daily_spend_record[str(current_date)]=daily_spend_record[str(current_date)]+price
                    with open("daily_spend_record.json", "w") as file2:
                        json.dump(daily_spend_record, file2)
                if str(current_date) not in daily_spend_record:
                    daily_spend_record[str(current_date)]=price
                    with open("daily_spend_record.json", "w") as file2:
                        json.dump(daily_spend_record, file2)

            except (IndexError, ValueError):
                logging.error("\n### Invalid category selection ###\n")

    if feature == 2:
        logging.info("\n##### Choose a category #####")
        cat_list = list(expense_data.keys())
        for idx, key in enumerate(cat_list, 1):
            logging.info(f"\t{idx}. {key}")

        try:
            category_total_list=[]
            enter_category = int(input("Choose a category to see total expense: ")) - 1
            for item in expense_data[cat_list[enter_category]]:
                category_total_list.append(item["price"])
            logging.info(f"\nThe total spent in {cat_list[enter_category]} is {sum(category_total_list)}")
            
        except (IndexError, ValueError):
            logging.error("\n### Invalid category selection ###\n")
        

    if feature == 3:
        total_exp=[]
        for categ,valeu in expense_data.items():
            for i in range (len(valeu)):
                total_exp.append(valeu[i]["price"])
        
        logging.info(f"\nTotal spent in all categories is {sum(total_exp)}")

    if feature == 4:
        logging.info("\n##### Expense History #####")
        for category, items in expense_data.items():
            logging.info(f"{category}")
            for item in items:
                for k, v in item.items():
                    logging.info(f"\t{k}: {v}")
                logging.info(" ")

    if feature == 5:
        logging.info("\n##### Choose a category #####")
        cat_list = list(expense_data.keys())
        
        try:
            
            category_total_list=[]
            category_lablelist=[]
            for category in cat_list:
                category_total=0
                category_lablelist.append(category)
                for item in expense_data[category]:
                    category_total+=int(item["price"])
                category_total_list.append(category_total)

            def make_autopct(values):
                def my_autopct(pct):
                    total = sum(values)
                    val = int(round(pct*total/100.0))
                    return 'total:{v:d} ({p:.1f}%)'.format(p=pct,v=val)
                return my_autopct
            
            font1 = {'family':'serif','color':'blue','size':20}
            plt.pie(category_total_list,labels=category_lablelist,autopct=make_autopct(category_total_list),radius=1.2)
            plt.title("total expense in different categorys",fontdict=font1)
            plt.legend()
            plt.show()
        except (IndexError, ValueError):
            logging.error("\n### Invalid category selection ###\n")

    if feature == 6:
        dayly_spent=[]
        dates=[]
        for k,v in daily_spend_record.items():
            dayly_spent.append(v)
            dates.append(k)
        plt.bar(dates,dayly_spent,width=.2)
        plt.title("Total spend record daily")
        plt.xlabel("Dates of total spends")
        plt.ylabel("daily total spend amount")
        plt.show()
      


    if feature == 7:
        logging.info("Exiting the application.")
        break
    