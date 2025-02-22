import os
import re
def name_valid():
    while True:
        name = input("enter  the name")
        if os.path.exists(name):
            print("File already exists")
        elif re.findall("[0-9]", name):
            print("Name should not contain numbers")
        else:
            f = open(name, "a")
            f.write(name)
            break
    while True:
        email = input("enter the email")
        if re.findall(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            f.write('\n'+email)
            break
        else:
            print("Enter a valid email id")
    while True:
        phone = input("Enter the phone number")
        if re.findall(r"^[0-9]{10}$", phone):
            f.write('\n' + phone)
            f.close()
            break
        else:
            print("Enter valid phone number")
def deltes():
    m = input("enter the file name")
    if os.path.exists(m):
        os.remove(m)
        print("deleted successfully")
    else:
        print("The file does not exist")

while True:
    print("1.creation \n2.deletion \n3.Exit")
    d = int(input("enter the choice"))
    if d==1:
        name_valid()
    elif d==2:
        deltes()
    elif d==3:
        exit()
    else:
        print("invalid entry ")