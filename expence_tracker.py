import json

expence_data={"feruts":{"apple":45,"banana":66}}
total_expence=[]

"""feature 1 to add expence ibn a paresent category or create a new category for add expence"""
choose_category=int(input("1.enter expence in peresent category\n2.enter expence to a new category\nEnter your choice:"))
if choose_category==1:
    while True:
        print(expence_data.keys())
        category=str(input("Enter category to add expence:"))

        """to add expence in cxpence_data dectionary"""
        expence_data[category]={(str(input("enter date of perchase"))):(int(input("enter prise you spend")))}

        """to store expences json format to a file"""
        with open("expence.json","w") as file:
            json.dump(expence_data)