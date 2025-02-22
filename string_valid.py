s=input("Enter a string")
a=s.count('*')
b=s.count('#')
if a>0 or b>0:
    if a>b:
        print("Positive integer")
    elif a<b:
        print("negative integer")
    else:
        print("Valid String")
else:
    print("Not a valid string")