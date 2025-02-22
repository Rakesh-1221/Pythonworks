a = int(input("Ente first number"))
b = int(input("Enter second number"))
def sum(a,b):
    s=a+b
    print("sum is",s)
def sub(a,b):
    s=a-b
    print("sub is",s)
def mul(a,b):
    s=a*b
    print("mul is",s)
def div(a,b):
    s=a/b
    print("div is",s)
while True:
    print("1.add \n2.sub \n3.mul \n4.div \n5.exit")
    c=int(input("Enter the choice"))
    if c==1:
        sum(a,b)
    elif c==2:
        sub(a,b)
    elif c==3:
        mul(a,b)
    elif c==4:
        div(a,b)
    elif c==5:
        exit()
    else:
        print("Invalid choice")


