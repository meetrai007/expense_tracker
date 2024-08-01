import json

with open ("expence_data.json","r") as f:
    expence_data=json.load(f)

total_expence=[]

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