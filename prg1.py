x=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(x)):
    if x[i]%2!=0:
        x[i]='&'
print(x[::-1])

"""x = [1, 2, 3, 4, 5]
x = ['&' if i % 2 != 0 else i for i in x]
print(x[::-1])"""

"""x=[1,2,3,4,5,6,7,8]
print(x[::-2])"""
