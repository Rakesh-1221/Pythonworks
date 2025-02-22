import pandas as pd
import os
def create():
  n=input("Enter the name")
  p=input("Enter the password")
  df=pd.DataFrame({"name":[n],"password":[p]})
  if os.path.exists("Sample.csv"):
    df.to_csv("sample.csv",mode='a',index=False,header=False)
  else:
    df.to_csv("sample.csv",index=False,header=True)

def login():
  na = input("Enter your name: ")
  pas = int(input("Enter the password: "))
  df=pd.read_csv("sample.csv")
  if ((df['name'] == na) & (df['password'] == pas)).any():
    print("Login successful!")
    exit()
  else:
    print("Login failed. Invalid name or password.")

while True:
  print("1.creation \n2.Login user \n3.Exit")
  d = int(input("enter the choice"))
  if d == 1:
    create()
  elif d==2:
    login()
  elif d==3:
    exit()
  else:
    print("Invalid Choice")




"""dict=[]
while True:
  print("1.creation \n2.Display  \n3.Login user \n4.Exit")
  d = int(input("enter the choice"))
  if d==1:
    entry={}
    entry["name"]=input("Enter your name")
    entry["password"]=int(input("Enter the password"))
    dict.append(entry)
    df=pd.DataFrame(dict)
    df.to_csv("sample.csv")
  elif d==2:
    print(df)
  elif d==3:
    na = input("Enter your name: ")
    pas = int(input("Enter the password: "))
    if ((df['name'] == na) & (df['password'] == pas)).any():
      print("Login successful!")
      exit()
    else:
      print("Login failed. Invalid name or password.")"""
