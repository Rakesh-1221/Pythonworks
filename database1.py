import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dtbase"
)
mycursor = mydb.cursor()
mycursor.execute("create table login (id int primary key auto_increment,username varchar(20),password varchar(20),phone varchar(20)")