import re
while True:
    phone = input("Enter the phone number")
    if re.findall(r"^[0-9]{10}$", phone):
        f = open("file.txt","a")
        f.write('\n' + phone)
        f = open("file.txt","r")
        print(f.read())
        f.close()
        break
    else:
         print("Enter valid phone number")
