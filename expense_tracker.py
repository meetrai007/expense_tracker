import json
import datetime

print("############## WELCOME TO EXPENSE TRACKER APPLICATION ##############")

# Load the expense data from the JSON file
try:
    with open("expensedata.json", "r") as file:
        expense_data = json.load(file)
except FileNotFoundError:
    expense_data = {}

current_date = datetime.date.today()

while True:
    try:
        feature = int(input("""   
                                1. Add expense
                                2. Total spend in a specific category
                                3. Total spends
                                4. View all expense history
                                5. Exit
                                Enter what you want to do: """))
    except ValueError:
        print("\n### Choose a valid option: 1, 2, 3, 4, or 5 ###\n")
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
                    print("\n### Enter details carefully ###\n")
                    continue
                
                if category not in expense_data:
                    expense_data[category] = []
                expense_data[category].append({"date": str(current_date), "description": description, "price": price})
                
                with open("expensedata.json", "w") as file:
                    json.dump(expense_data, file)
                
                continuty = str(input("Enter 'y' to add more expenses or 'n' to exit (y/n): "))

        if choice == 2:
            print("\n##### Choose a category #####")
            cat_list = list(expense_data.keys())
            for idx, key in enumerate(cat_list, 1):
                print(f"\t{idx}. {key}")

            try:
                enter_category = int(input("Choose a category in which you want to add expense: ")) - 1
                description = str(input("Write a short description of the spend: "))
                price = float(input("Enter the amount you spent: "))
                
                expense_data[cat_list[enter_category]].append({"date": str(current_date), "description": description, "price": price})
                with open("expensedata.json", "w") as file:
                    json.dump(expense_data, file)
            except (IndexError, ValueError):
                print("\n### Invalid category selection ###\n")

    if feature == 2:
        print("\n##### Choose a category #####")
        cat_list = list(expense_data.keys())
        for idx, key in enumerate(cat_list, 1):
            print(f"\t{idx}. {key}")

        try:
            enter_category = int(input("Choose a category to see total expense: ")) - 1
            category_total = sum(item["price"] for item in expense_data[cat_list[enter_category]])
            print(f"\nThe total spent in {cat_list[enter_category]} is {category_total}")
        except (IndexError, ValueError):
            print("\n### Invalid category selection ###\n")

    if feature == 3:
        category_total = sum(item["price"] for category in expense_data.values() for item in category)
        print(f"\nTotal spent in all categories is {category_total}")

    if feature == 4:
        print("\n##### Expense History #####")
        for category, items in expense_data.items():
            print(f"{category}")
            for item in items:
                for k, v in item.items():
                    print(f"\t{k}: {v}")
                print(" ")

    if feature == 5:
        print("Exiting the application.")
        break
