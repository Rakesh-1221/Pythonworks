n=int(input("enter a nmber"))
def facto(n):
    if n==0:
        return 1
    elif n<0:
        #print("Can't possible")
        return "not possible"
    else:
        fact=n*facto(n-1)
        return fact
print(facto(n))