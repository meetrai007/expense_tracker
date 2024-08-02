import json

with open ("expense_data.json","r") as f:
    expense_data=json.load(f)

tcost=[]
# total_expense=[]

while True:
    while True:
        try:
            feature=int(input("\n1.add expense\n2.totel spend in a special category\n3.total spends\n4.exit\nEnter what you do:"))
            break
        except Exception as e:
            print("\n### choose a valid option 1 or 2 or 3 or 4 ###\n")


    if feature==1:
        """feature 1 to add expense ibn a paresent category or create a new category for add expense"""
        while True:
            try:
                choose_category=int(input("1.enter expense in peresent category\n2.Create new category\nEnter your choice:"))
                break
            except ValueError:
                print("\n### choose a valid option 1 or 2 ###\n")
        
        if choose_category==1:
            continuty="y"
            while continuty != "n":
                while True:
                    try:
                        for categ in expense_data.keys():
                            print(categ)
                        category=str(input("Choose category to add expense:"))
                        """to add expense in expense_data dectionary"""
                        expense_data[category][(str(input("enter date of perchase:")))]=(int(input("enter prise you spend:")))
                        continuty=str(input("entre y to add more expense or n to exit y/n:"))
                        break
                    except:
                        print("\n### Enter a valid category showing bellow ###\n")

            """to store expenses json format to a file"""
            with open("expense_data.json","w") as file:
                json.dump(expense_data, file)

        if choose_category==2:
            while True:
                try:
                    new_cetegory=str(input("Enter a name for new category:"))
                    break
                except:
                    print("\n### Enter a valid category name try different ###\n")
            expense_data[new_cetegory]={}

            """to store new category in json """
            with open("expense_data.json","w") as file:
                json.dump(expense_data, file)

    if feature==2:
        """feature 2 to chect total spend in a special category"""
        while True:
            try:
                for categ in expense_data.keys():
                    print(categ)
                tspend_category=str(input("Choose category to see total expense:"))
                print(tspend_category)
                for k,v in expense_data[tspend_category].items():
                    print(f"\t{k} : {v}")
                    tcost.append(v)
                print(f"total spend in {tspend_category} is {sum(tcost)}")
                tcost.clear()
                break
            except:
                print("\n### Choose a valid category to see total expense ###\n")
        

    if feature==3:
        """feature 3 to chect total spend in all categorys"""
        for key in expense_data.keys():
            print(key)
            for k,v in expense_data[key].items():
                print(f"\t{k} : {v}")
                tcost.append(v)
        print(f"total spend in all category is {sum(tcost)}")
        tcost.clear()

    if feature==4:
        """to exit the application""" 
        break 
