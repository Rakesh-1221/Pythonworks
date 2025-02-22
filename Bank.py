import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dtbase"
)
mycursor = mydb.cursor()

#mycursor.execute("create table bank_acc(acc_no BIGINT primary key auto_increment ,acc_name varchar(20),phone varchar(20),balance decimal(10,2) not null default 1000.00)")

mycursor.execute("alter table bank_acc auto_increment=1000000000")
def acc_creation():
    name = input("Enter the name of account holder")
    ph = input("Enter the phone number")
    query="select acc_name,phone from bank_acc where acc_name=%s and phone=%s"
    mycursor.execute(query,(name,ph))
    check=mycursor.fetchone()
    if check:
        print("Username and password already existed")
    else:
        sql = "insert into bank_acc(acc_name,phone)values(%s,%s)"
        mycursor.execute(sql, (name, ph))
        mydb.commit()
        print("Account created successfully")
def login():
    user = input("Enter the username")
    num = int(input("Enter the account number:"))
    sql = "select acc_name,acc_no from bank_acc where acc_name=%s and acc_no=%s"
    mycursor.execute(sql, (user,num))
    check = mycursor.fetchone()
    if check:
        print("USER LOGIN SUCCESSFUL")
        while True:
            print("1.Deposit \n2.Withdraw \n3.Display Details\n4.Exit")
            ch = int(input("Enter the choice"))
            if ch == 1:
                deposit(num,user)
            elif ch == 2:
                withdraw(num,user)
            elif ch == 3:
                display(num,user)
            elif ch == 4:
                break
            else:
                print("Invalid Choice")
    else:
        print("Incorrect username or account number!!Please try again")
def deposit(num,user):
    amount = int(input("Enter the amount to be inserted"))
    q = "update bank_acc set balance=balance+%s where acc_no=%s and acc_name=%s "
    mycursor.execute(q, (amount, num,user))
    mydb.commit()
    print("Amount deposited successfully")

def withdraw(num,user):
    amount = int(input("Enter the amount to withdraw"))
    a = "Select balance from bank_acc where acc_no=%s and acc_name=%s"
    mycursor.execute(a, (num,user))
    bal = mycursor.fetchone()
    current_bal = bal[0]
    if current_bal >= 1000 and current_bal > amount:
        if current_bal - amount >= 1000:
            b = "update bank_acc set balance=balance-%s where acc_no=%s"
            mycursor.execute(b, (amount, num))
            mydb.commit()
            print("Amount withdraw successfully")
        else:
            print("Insufficient funds. Minimum balance of 1000 must be maintained.")
    else:
        print("Insufficient funds or withdrawal amount exceeds current balance.")
def display(num,user):
    sql = "Select * from bank_acc where acc_no=%s and acc_name=%s"
    mycursor.execute(sql, (num,user))
    details = mycursor.fetchall()
    for i in details:
        print(i)

while True:
    print("1.Account creation \n2.login \n3.exit")
    c = int(input("Enter the choice"))
    if c == 1:
        acc_creation()
    elif c == 2:
        login()
    elif c == 3:
        exit()
    else:
        print("Invalid choice")

mycursor.close()
mydb.close()
