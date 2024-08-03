import json
import datetime

print("############## WELCOME TO EXPENSE TRACKER APPLICATION ##############")

with open("expense_store.json","r") as file:
    expense_data=json.load(file)

# data_list=[]
cat_list=[]
category_total=0
tcost=[]
current_date = datetime.date.today()

# expense_data={}
# total_expense=[]

while True:
    while True:
        try:
            feature=int(input("""   
                                    1.add expens
                                    2.totel spend in a special category
                                    3.total spends
                                    4.exit
                                    Enter what you do:"""))
            break
        except Exception as e:
            print("\n### choose a valid option 1 or 2 or 3 or 4 ###\n")


    if feature==1:
        """feature 1 to add expense in a paresent category or create a new category for add expense"""

        """ther are make two featue to add expense with new category on in paresent category by user choise in choice"""
        choice=int(input("""##### now choose a option #####
                                    1.add expense in with new category
                                    2.add expense in paresent category
                                    Enter your choice 1 or 2 :"""))
        if choice==1:
            continuty="y"
            while continuty != "n":
                try:
                    category=str(input("Enter Category in witch you spend:"))
                    dicription=str(input("Write short decription of spend:"))
                    prise=int(input("enter prise you spend:"))
                except:
                    print("\n### Enter detail carefully ###\n")
                    continue
                
                data_list=[{"date":str(current_date),"dicription":dicription,"prise":prise,}]
                # expense_data[category]=({"date":str(current_date),"dicription":dicription,"prise":prise,})
                expense_data[category]=data_list
                
                """to store expenses json format to a file"""
                with open("expense_store.json","w") as file:
                    json.dump(expense_data,file)
                
                continuty=str(input("Enter y to add more expense or n to exit y/n:"))
        

        if choice==2:
            print("\n##### choose a category #####")
            num=1
            for key in expense_data:
                print(f"\t{num}.{key}")
                num+=1
                cat_list.append(key)

            """get input by user to add new data in present category"""
            enter_category=int(input("\tchoose a category in witch you want to add expense:"))-1
            dicription=str(input("Write short decription of spend:"))
            prise=int(input("enter prise you spend:"))

            """to store data in present category"""
            new_data={"date":str(current_date),"dicription":dicription,"prise":prise,}
            expense_data[cat_list[enter_category]].append(new_data)
            with open("expense_store.json","w") as file:
                    json.dump(expense_data,file)

    if feature==2:
        """feature 2 to chect total spend in a special category"""
        while True:
            try:
                num=1
                for key in expense_data:
                    print(f"\t{num}.{key}")
                    num+=1
                    cat_list.append(key)

                """get input by user to see total expense of a category"""
                enter_category=int(input("choose a category in witch you want to add expense:"))-1
                
                for items in expense_data[cat_list[enter_category]]:
                    category_total+=items["prise"]
                break
            except:
                print("\n### Choose a valid category to see total expense ###\n")
                continue
        print(f"the total spent in {cat_list[enter_category]} is {category_total}")
        category_total=0
        

    if feature==3:
        """feature 3 to chect total spend in all categorys"""
        for key in expense_data:
            print(key)
            for items in expense_data[key]:
                category_total+=items["prise"]
                
            
        print(f"total spend in all category is {category_total}")
        category_total=0

    if feature==4:
        """to exit the application""" 
        break 
