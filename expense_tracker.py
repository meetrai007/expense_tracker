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
        while True:
            try:
                choice = int(input("""##### Choose an option #####
                                        1. Add expense in new category
                                        2. Add expense in existing category
                                        3. back
                                        Enter your choice (1 or 2): """))
            except ValueError:
                logging.info("\n### Choose a valid option: 1, 2, 3 ###\n")
                continue
            if choice == 1:
                continuty = "y"
                while continuty.lower() != "n":
                    while True:
                        try:
                            category = str(input("Enter category in which you spent: "))
                            break
                        except ValueError:
                            logging.info("expense not added")
                            logging.warning("\n### Enter details carefully and in wright format ###\n")
                    description = str(input("Write a short description of the spend: "))
                    while True:
                        try:
                            price = float(input("Enter the amount you spent: "))
                            break
                        except ValueError:
                            logging.info("expense not added")
                            logging.warning("\n### Enter details carefully and in wright format ###\n")

                        

                    if category not in expense_data:
                        expense_data[category] = []
                    expense_data[category].append({"date": str(current_date), "description": description, "price": price})
                    
                    with open("expensedata.json", "w") as file:
                        json.dump(expense_data, file)
                    logging.info("expense added")

                    
                    continuty = str(input("Enter 'y' to add more expenses or 'n' to exit (y/n): "))

            elif choice == 2:
                logging.info("\n##### Choose a category #####")
                cat_list = list(expense_data.keys())
                for idx, key in enumerate(cat_list, 1):
                    logging.info(f"\t{idx}. {key}")
                while True:
                    try:
                        enter_category = int(input("Choose a category in which you want to add expense: ")) - 1
                        break
                    except (IndexError, ValueError):
                        logging.error("\n### Invalid category selection ###\n")

                description = str(input("Write a short description of the spend: "))
                while True:
                    try:
                        price = float(input("Enter the amount you spent: "))
                        break
                    except (IndexError, ValueError):
                        logging.error("\n### Invalid prise input ###\n")
                    
                expense_data[cat_list[enter_category]].append({"date": str(current_date), "description": description, "price": price})
                with open("expensedata.json", "w") as file:
                    json.dump(expense_data, file)
                logging.info("expense adeed")

            elif choice==3:
                break
            else:
                print("invalid choice,please enter 1 or 2 only")

    elif feature == 2:
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
        

    elif feature == 3:
        total_exp=[]
        for categ,valeu in expense_data.items():
            for i in range (len(valeu)):
                total_exp.append(valeu[i]["price"])
        
        logging.info(f"\nTotal spent in all categories is {sum(total_exp)}")

    elif feature == 4:
        logging.info("\n##### Expense History #####")
        for category, items in expense_data.items():
            logging.info(f"{category}")
            for item in items:
                for k, v in item.items():
                    logging.info(f"\t{k}: {v}")
                logging.info(" ")

    elif feature == 5:
        logging.info("\n##### Choose a category #####")
        
        
        try:
            start_date = datetime.datetime.strptime(input("Enter the start date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(input("Enter the end date (YYYY-MM-DD): "), "%Y-%m-%d").date()

            filtered_expenses = {}
            for category, items in expense_data.items():
                for item in items:
                    item_date = datetime.datetime.strptime(item["date"], "%Y-%m-%d").date()
                    if start_date <= item_date <= end_date:
                        if category not in filtered_expenses:
                            filtered_expenses[category] = 0
                        filtered_expenses[category] += item["price"]
                        

            def make_autopct(values):
                def my_autopct(pct):
                    total = sum(values)
                    val = int(round(pct*total/100.0))
                    return 'total:{v:d} ({p:.1f}%)'.format(p=pct,v=val)
                return my_autopct
            
            if filtered_expenses:
                # Plotting the pie chart
                plt.figure(figsize=(8, 6))
                plt.pie(filtered_expenses.values(), labels=filtered_expenses.keys(), autopct=make_autopct(list(filtered_expenses.values())), startangle=140)
                plt.title(f"Expenses Distribution from {start_date} to {end_date}")
                plt.legend()
                plt.show()

        except (IndexError, ValueError):
            logging.error("\n### Invalid category selection or dateinput ###\n")

    elif feature == 6:
        try:
            start_date = datetime.datetime.strptime(input("Enter the start date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(input("Enter the end date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        except:
            print("please enter valid datetime in right formet")
            continue
        
        dayly_spent={}
        
        for categoreys in expense_data.keys():
            for list in expense_data[categoreys]:
                todaydate=datetime.datetime.strptime(list["date"], "%Y-%m-%d").date()
                if start_date<=todaydate<=end_date:
                    dayly_spent[list["date"]]=0
                    dayly_spent[list["date"]]+=list["price"]
                    
        plt.bar(dayly_spent.keys(),dayly_spent.values(),width=.2)
        plt.title("Total spend record daily")
        plt.xlabel("Dates of total spends")
        plt.ylabel("daily total spend amount")
        plt.show()
      


    elif feature == 7:
        logging.info("Exiting the application.")
        break
    
    else:
        print("invalid choice, please enter choice between 1 to 7 only")