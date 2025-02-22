list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x=[]
for i in list:
    if i%2!=0 and i%3==0:
        x.append(i)
print(x)
print(sum(x))

"""def sum_except_even_divisible_by_3(lst):
    total_sum = 0
    for num in lst:
        if num % 2 != 0 or num % 6 != 0:
            total_sum += num
    return total_sum
my_list = [1, 2, 3, 4, 5, 6, 9,10,11,12,13,14,15]
result = sum_except_even_divisible_by_3(my_list)
print("Sum of list elements except even numbers divisible by 3:", result)"""
