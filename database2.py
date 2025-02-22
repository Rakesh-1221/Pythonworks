import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dtbase"
)
mycursor = mydb.cursor()


def inst():
    na = input("Enter the username")
    ps = input("Enter the password")
    ph = input("Enter the phone number")
    s = "select * from login where username=%s or password=%s"
    mycursor.execute(s, (na, ps))
    check = mycursor.fetchall()
    if check:
        print("username and password already inserted")
    else:
        sql = "INSERT INTO login(username,password,phone) VALUES (%s, %s,%s)"
        val = (na, ps, ph)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Record inserted")


def read():
    mycursor.execute("select * from login")
    result = mycursor.fetchall()
    for x in result:
        print(x)


def updte():
    while True:
        ab = int(input("Enter the id to be updated"))
        s = "select id from login where id=%s"
        mycursor.execute(s, (ab,))
        dt = mycursor.fetchone()
        if dt:
            c = int(input("choose the option for updation \n1.username \n2.password \n3.phone \n4.exit "))
            if c == 1:
                upt = input("Enter the new value")
                sql = "update login set username = %s where id=%s"
                mycursor.execute(sql, (upt, ab))
                mydb.commit()
                print(mycursor.rowcount, "record effected")
                break
            elif c == 2:
                upt = input("Enter the new value")
                sql = "update login set password= %s where id=%s"
                mycursor.execute(sql, (upt, ab))
                mydb.commit()
                print(mycursor.rowcount, "record effected")
                break
            elif c == 3:
                upt = input("Enter the new value")
                sql = "update login set phone = %s where id=%s"
                mycursor.execute(sql, (upt, ab))
                mydb.commit()
                print(mycursor.rowcount, "record effected")
                break
            elif c == 4:
                break
            else:
                print("Invalid Choice")
                break
        else:
            print("Enter valid id!!!!! ")


def dlete():
    deleted_one = input("enter the id of deleting item")
    sql = "DELETE FROM login WHERE id = %s"
    val = (deleted_one,)
    mycursor.execute(sql, val)
    mydb.commit()
    if mycursor.rowcount > 0:
        print(mycursor.rowcount, "rows deleted")
    else:
        print("The required id not find")


while True:
    print("1.Insertion \n2.Display \n3.Updating \n4.Deletion \n5.Exit")
    ch = int(input("Enter the choice"))
    if ch == 1:
        inst()
    elif ch == 2:
        read()
    elif ch == 3:
        updte()
    elif ch == 4:
        dlete()
    elif ch == 5:
        exit()
    else:
        print("Invalid Choice")

mycursor.close()
mydb.close()
