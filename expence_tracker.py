import json

with open ("expence_data.json","r") as f:
    expence_data=json.load(f)

tcost=[]
# total_expence=[]

feature=int(input("\n1.add expence\n2.totel spend in a special category\n3.total spends\nEnter what you do:"))

if feature==1:
    """feature 1 to add expence ibn a paresent category or create a new category for add expence"""
    choose_category=int(input("1.enter expence in peresent category\n2.Create new category\nEnter your choice:"))
    if choose_category==1:
        continuty="y"
        while continuty != "n":
            print(expence_data.keys())
            category=str(input("Enter category to add expence:"))

            """to add expence in expence_data dectionary"""
            expence_data[category][(str(input("enter date of perchase:")))]=(int(input("enter prise you spend:")))
            continuty=str(input("entre y to add more expence or n to exit y/n:"))

        """to store expences json format to a file"""
        with open("expence_data.json","w") as file:
            json.dump(expence_data, file)

    if choose_category==2:
        new_cetegory=str(input("Enter new category name:"))
        expence_data[new_cetegory]={}

        """to store new category in json """
        with open("expence_data.json","w") as file:
            json.dump(expence_data, file)

if feature==2:
    """feature 2 to chect total spend in a special category"""
    print(expence_data.keys())
    tspend_category=str(input("Choose category to check total spend:"))
    print(tspend_category)
    for k,v in expence_data[tspend_category].items():
        print(f"\t{k} : {v}")
        tcost.append(v)
    print(f"total spend in {tspend_category} is {sum(tcost)}")
    tcost.clear()

if feature==3:
    """feature 3 to chect total spend in all categorys"""
    for key in expence_data.keys():
        print(key)
        for k,v in expence_data[key].items():
            print(f"\t{k} : {v}")
            tcost.append(v)
    print(f"total spend in all category is {sum(tcost)}")
    tcost.clear()
    
