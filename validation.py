dict={}
dict["name"]=input("Enter the name")
dict["password"]=int(input("Enter the password"))
print("please login")
n=input("Ente the name")
pa=int(input("Enter password"))
if dict["name"]==n and dict["password"]==pa:
    print("Login Successfully")
else:
    print("invalid username and password")