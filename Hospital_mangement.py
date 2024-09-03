import pymongo
import re
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["Hospital"]
myco = mydb["doctors_data"]
myc = mydb["booking_details"]


def patient_reg():
    user_data = {}
    last_patient = mycol.find_one(sort=[("user_id", -1)])
    if last_patient and "user_id" in last_patient:
        user_id = last_patient["user_id"] + 1
    else:
        user_id = 1000
    user_data["user_id"] = user_id
    while True:
        user_data["name"] = input("Enter your name")
        if not re.match(r"^[A-Za-z]", user_data["name"]):
            print("Name must contain only alphabetic characters")
        else:
            break
    while True:
        user_data["password"] = input("Enter the Password")
        if len(user_data["password"]) < 8:
            print("Password must contain 8 or more characters")
        elif not re.search(r"^[A-Z]", user_data["password"]):
            print("Password must be start with Capital letters ")
        elif not re.search(r"[a-z]", user_data["password"]):
            print("Password must contain at least one lower case alphabet ")
        elif not re.search(r"[!@#$%^&*]", user_data["password"]):
            print("Password must contain at least one special character")
        elif not re.search("[0-9]", user_data["password"]):
            print("Password must contain at least one digit")
        else:
            break
    while True:
        user_data["gender"] = input("Enter the gender")
        if not re.match(r"^[A-Za-z]", user_data["gender"]):
            print("gender should be alphabetic characters")
        else:
            break
    while True:
        user_data["age"] = input("Enter your age")
        if not re.match(r"^[0-9]", user_data["age"]):
            print("age should be digits")
        else:
            break
    while True:
        user_data["blood"] = input("Enter the blood group")
        if not re.match(r"^(A|B|AB|O|a|b|ab|o)[+-]$", user_data["blood"]):
            print("Invalid blood type.Please enter a valid blood type (e.g., A+, O-, etc.).")
        else:
            break
    while True:
        user_data["phone"] = input("Enter the phone number")
        if not re.match(r"^[0-9]", user_data["phone"]):
            print("Phone number should be digits")
        elif len(user_data["phone"]) < 10:
            print("phone number must contain 10 digits")
        else:
            break
    while True:
        user_data["email"] = input("Enter the email")
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", user_data["email"]):
            print("Email must be in a correct format")
        else:
            break
    user_data["address"] = input("Enter the address")
    mycol.insert_one(user_data)
    print("Data inserted successfully with patient id", user_data["user_id"])


def doctor_reg():
    doc_data = {}
    last_doctor = myco.find_one(sort=[("doctor_id", -1)])
    if last_doctor and "doctor_id" in last_doctor:
        doctor_id = last_doctor["doctor_id"] + 1
    else:
        doctor_id = 100
    doc_data["doctor_id"] = doctor_id
    while True:
        doc_data["name"] = input("Enter your name")
        if not re.match(r"^[A-Za-z]", doc_data["name"]):
            print("Name must contain only alphabetic characters")
        else:
            break
    while True:
        doc_data["password"] = input("Enter the Password")
        if len(doc_data["password"]) < 8:
            print("Password must contain 8 or more characters")
        elif not re.search(r"^[A-Z]", doc_data["password"]):
            print("Password must be start with Capital letters ")
        elif not re.search(r"[a-z]", doc_data["password"]):
            print("Password must contain at least one lower case alphabet ")
        elif not re.search(r"[!@#$%^&*]", doc_data["password"]):
            print("Password must contain at least one special character")
        elif not re.search("[0-9]", doc_data["password"]):
            print("Password must contain at least one digit")
        else:
            break
    while True:
        doc_data["gender"] = input("Enter the gender")
        if not re.match(r"^[A-Za-z]", doc_data["gender"]):
            print("gender should be alphabetic characters")
        else:
            break
    while True:
        doc_data["department"] = input("Enter the department name")
        if not re.match(r"^[A-Za-z]", doc_data["department"]):
            print("department name must contain only alphabetic characters")
        else:
            break
    while True:
        doc_data["phone"] = input("Enter the phone number")
        if not re.match(r"^[0-9]", doc_data["phone"]):
            print("Phone number should be digits")
        elif len(doc_data["phone"]) < 10:
            print("phone number must contain 10 digits")
        else:
            break
    while True:
        doc_data["email"] = input("Enter the email")
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", doc_data["email"]):
            print("Email must be in a correct format")
        else:
            break
    doc_data["address"] = input("Enter the address")
    myco.insert_one(doc_data)
    print("Data inserted successfully with the doctor id", doc_data["doctor_id"])


def token_gen(doctor_id):
    today_date = datetime.now().strftime('%Y-%m-%d')

    #find the last token of the doctor on today's date
    last_booking = myc.find_one({"doctor_id": doctor_id, "date": today_date}, sort=[("Token", -1)])

    if last_booking:
        new_token = last_booking["Token"] + 1
    else:
        new_token = 1

    return new_token


def login_patient():
    pid = int(input("Enter the user id"))
    pas = input("Enter the password")
    check_user = mycol.find_one({"user_id": pid, "password": pas})
    if check_user:
        print("Patient Login Successful")
        print("\nSelect the department")
        department_list = myco.distinct("department")
        index = 1
        for department in department_list:
            print(str(index) + ". " + department)
            index += 1
        dep_choice = int(input("Enter the choice:"))
        selected_department = department_list[dep_choice - 1]

        print("list of available doctors")
        doctors_cursor = myco.find({"department": selected_department}, {"_id": 0, "doctor_id": 1, "name": 1})
        d_list = list(doctors_cursor)
        d_index = 1
        for doc in d_list:
            print(str(d_index) + "." + "Dr. " + doc['name'] + "[ID:" + str(doc['doctor_id']) + "]")
            d_index += 1

        doc_choice = int(input("Select the choice for  doctor:"))
        selected_doctor = d_list[doc_choice - 1]

        #name and id assigned to each variable
        doctor_id = selected_doctor['doctor_id']
        doctor_name = selected_doctor['name']

        Token = token_gen(doctor_id)

        bookings = {
            "patient_id": pid,
            "patient_name": check_user["name"],
            "doctor_id": doctor_id,
            "doctor_name": doctor_name,
            "department": selected_department,
            "Token": Token,
            "date": datetime.now().strftime('%Y-%m-%d'),
            "Status": "Booked"
        }
        myc.insert_one(bookings)
        print("Booking successful with token number", Token)
    else:
        print("Incorrect password or patient not found")


def login_doctor():
        pid = int(input("Enter the doctor id"))
        pas = input("Enter the password")
        check_user = myco.find_one({"doctor_id": pid, "password": pas})
        if check_user:
            print("Doctor Login Successful")
            fetch_bookings = myc.find({"doctor_id": pid}, {"_id": 0, "patient_name": 1, "Token": 1, "Status": 1,"date":1})
            booking_list = list(fetch_bookings)
            to_date = datetime.now().strftime('%Y-%m-%d')
            b_index = 1
            for book in booking_list:
                if book['date'] == to_date:
                    print(str(b_index) + "." + "patient name:" + book['patient_name'] + " With Token number :" + str(book['Token']) + " Status : " + book["Status"] + ", On " + str(book['date']))
                    b_index += 1
        else:
            print("Incorrect password or doctor not found")


while True:
    choice = int(input("Hospital management System \n1.Registration \n2.Login \n3.Exit \nEnter the choice:"))
    if choice == 1:
        r_ch = int(input("1.Patient \n2.Doctor \n3.Exit \nSelect the option"))
        if r_ch == 1:
            doctor_reg()
        elif r_ch == 2:
            patient_reg()
        elif r_ch == 3:
            break
        else:
            print("Invalid choice")
    elif choice == 2:
        r_ch = int(input("1.Patient \n2.Doctor \n3.Exit \nSelect the option"))
        if r_ch == 1:
            login_patient()
        elif r_ch == 2:
            login_doctor()
        elif r_ch == 3:
            break
        else:
            print("Invalid choice")
    elif choice == 3:
        exit()
    else:
        print("Invalid choice")
