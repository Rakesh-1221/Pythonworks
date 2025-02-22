"""s=input("Enter the string")
b=""
for i in s:
    if i in ("@","%","*","$",".","#"):
        continue
    else:
        b+=i
print(b)"""

a=input("enter string")
q="!@#$%^&*"
c=""
for i in a:
    if i not in q:
        c+=i
print(c)
