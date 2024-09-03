import pymongo
import re
from pymongo.errors import DuplicateKeyError

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["crud_data"]

mycol.create_index("phone", unique=True)


def inst():
    while True:
        dict={}
        while True:
            dict["name"] = input("Enter the name")
            if re.match("[a-zA-Z]",dict["name"]):
                break
            print("Name should be characters")

        while True:
            dict["password"] = input("Enter the password")
            if re.match(r"^[A-Z][A-Za-z0-9!@#$%^&*]{7,}$",dict["password"]):
                break
            print("password must be correct format")

        while True:
            dict["phone"] = input("Enter the phone number")
            if re.match(r"^[0-9]{10}$",dict["phone"]):
                existing_ph = mycol.find_one({"phone": dict["phone"]})
                if existing_ph:
                    print("User with phone number already exist")
                else:
                    break
            else:
                print("Phone number must be contain 10 digits")

        dict["address"] = input("Enter the address")
        mycol.insert_one(dict)
        print("Data inserted successfully")
        break
def updte():
    while True:
        ph = input("Enter the phone number")
        check = mycol.find_one({"phone": ph})
        if check:
            c = int(input("Select the key to be updated \n1.name \n2.Password \n3.phone \n4.address"))
            if c == 1:
                name = input("Enter the new name")
                query = {"phone": ph}
                new = {"$set": {"name": name}}
                mycol.update_one(query, new)
                print("Name updated successfully")
                break

            elif c == 2:
                pas = input("Enter the new password")
                query = {"phone": ph}
                new = {"$set": {"password": pas}}
                mycol.update_one(query, new)
                print("Password updated successfully")
                break

            elif c == 3:
                phone = input("Enter the new phone number")
                try:
                    query = {"phone": ph}
                    new = {"$set": {"phone": phone}}
                    mycol.update_one(query, new)
                    print("Phone number updated successfully")
                    break
                except DuplicateKeyError:
                    print("User with phone number already exist")

            elif c == 4:
                addr = input("Enter the new phone number")
                query = {"phone": ph}
                new = {"$set": {"password": addr}}
                mycol.update_one(query, new)
                print("Phone number updated successfully")
                break

            elif c == 5:
                exit()
            else:
                print("Invalid Choice")
        else:
            print("Enter a correct phone number")


def delte():
    while True:
        ph = input("Enter the phone number")
        check = mycol.find_one({"phone": ph})
        if check:
            query = {"phone": ph}
            mycol.delete_one(query)
            print("Item deleted successfully")
            break
        else:
            print("invalid Phone number!!!")
def disply():
    ph = input("Enter the phone number")
    data = mycol.find({"phone": ph})
    for x in data:
        print(x)

while True:
    c = int(input("Select the choice \n1.Insertion \n2.Updation \n3.Deletion \n4.Display details \n5.Exit"))
    if c == 1:
        inst()
    elif c == 2:
        updte()
    elif c == 3:
        delte()
    elif c == 4:
        disply()
    elif c == 5:
        exit()
    else:
        print("Invalid choice")
