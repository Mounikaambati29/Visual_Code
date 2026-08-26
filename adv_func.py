# Quiz
# 1.What is the purpose of the map() function in Python
# [b] To apply a function to each element of an iterable

# 2.Which of the following functions is NOT a part of the functools module
# [a] map()

# 3. What does the filter() function do
# [c]  Filters elements from an iterable based on a condition(function returns True)

# 4. In Python, what is the purpose of the reduce() function
# [d] To apply a function to pairs of elements in an iterable until it's reduced to a single value



#PRACTICE

# 1.
# def add(a,b):
#     return a+b
# obj=add(18,26)
# print(obj)
# result = lambda a,b: a+b
# print(result(38,42))


# 2. filter--> filter(function,iterable)

# list_1=[28,42,817,9,26,832,49,144,9,60,3]
# empty_list=[]
# for i in list_1:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)

# 3.
# def even(a):
#     return a%2==0
# obj=even(82)
# print(obj)

# 4.
# list_1=[298,42,16,4,89,55,69,12,8,34]
# def even(a):
#     return a%2==0
# result=filter(even,list_1)
# print(list(result))
#   (or)
# list_1=[298,42,16,4,89,55,69,12,8,34]
# result=filter(lambda a:a%2==0, list_1)
# print(list(result))

# 5.
# list_1=[298,42,16,4,89,55,69,12,8,34]
# def squares(a):
#     return a**2
# result = map(squares,list_1)
# print(list(result))

# 6.
# list_1=[298,42,16,4,89,55,69,12,8,34]
# list_2=[38,42,692,888,247,31,90,58,12]
# result=map(lambda a,b : a**b, list_1,list_2)
# print(list(result))
# 7.
list_3=[1,1,2,2,3,3,4,7,6,4,7,6,5,8,9,5,9,8]
result=map(lambda a: a**2,list_3)
print(list(result))
# 8.
List_4=(-6,-2,8,1,66,948,-9,12,91,72,-8,-1,-4,-8)
result=filter(lambda a: a>=0,List_4)
print(list(result))
# 9.
from functools import reduce
list_5=[2,2,32,3,4,3,435,534,5345,64,]
result=reduce(lambda a,b:a*b, list_5)
print(result)
# 10.
string="today i am learing python in my pyhton_life channel"
vovels="AEIOUaeiou"
result=reduce(lambda a,b: a+[b] if b in vovels else a, string,[])
print(len(result))





