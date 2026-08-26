#Quiz
# Question 1:
# What does the all() function return when applied to an empty tuple
# [a] True

# Question 2:
# Which of the following statements correctly creates a tuple
#  [b] my_tuple = (1, 2, 3)

# Question 3:
# What is the output of the following code snippet?
# my_tuple = (1, 2, 3)
# print(len(my_tuple))
# [c] 3

# Question 4:
# Which of the following statements about tuples in Python is true
# [c] Tuples use parenthesis ( ) for declaration


#Coding Exercise:

# 1. Create a Tuple: Write a program that creates a tuple containing three elements:
# your name, your age, and your favorite color. Then print the tuple

t={"moni",18,"black"}
print(t)

# 2. Access Tuple Elements: Write a program that creates a tuple containing the
# days of the week. Then, print the third element of the tuple

tuple_1=("Sunday", "Monday", "Tuesday", "Wednesday", "THursday", "Friday", "Saturday")
print(tuple_1[2])
print(tuple_1[ :4])
print(tuple_1[2:5])
print(tuple_1.index("Wednesday"))

# 3. Tuple Concatenation: Write a program that creates two tuples, one
# containing odd numbers from 1 to 5 and another containing even numbers
# from 2 to 6. Concatenate these two tuples and print the result.

t_1=(1,3,5)
t_2=(2,4,6)
result=t_1+t_2
print(result)

# 4. Tuple Unpacking: Write a program that defines a tuple containing the
# dimensions of a rectangle (length and width). Then, unpack this tuple into
# two variables and calculate the area of the rectangle.

tuple_1=(20,2)
length,width=tuple_1
area= length *width
print(area)

# 5. Check if an Element Exists: Write a program that checks if a given element exists in a tuple

number=(1,2,3,4,5,6,7,8)
element=int(input("enter the exits number"))

if element in number:
    print("exit")
else:
    print("not exits")

# 6. Write a Python program to generate a bill for a supermarket purchase. The program should
# store the items and their prices in a list of tuples. It shouldthen iterate over this list to
# print out each item along with its price.Finally,calculate & print total cost of all the items
# Sample Input:
# items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
# Sample Output:
# Item Price
# --------------------
# Apple 99.00
# Banana 99.00
# Milk 49.00
# --------------------
# Total 247.00

items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
print("items\t price")
print("-"*20)
sum=0
for i, j in items:
    sum+=j
    print(f"{i}\t{j:.3f}")
print("-"*20)
print(f"total\t{sum:.3f}")
