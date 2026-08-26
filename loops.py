#Quiz  (day 6)
#1)  What is the purpose of the for loop in Python?
#[b]To repeatedly execute a block of code for each element in a sequence

#2) How do you iterate over a range of numbers in a for loop
#[b]Using the range() function

#3) When does a while loop stop executing
#[b] When the loop condition becomes false

#4) What does the while loop syntax look like in Python
#[c]while condition

#Exercises:

# 1) The sum of the squares of numbers from 1 to 5 using a for loop
sum=0
for i in range(1,6):
    sum=sum+i**2
    print(sum)
print("Sum of Squares =", sum)

# 2) Write a Python program that uses a while loop to print a countdown from 5 to 1
i = 5
while i >= 1:
    print(i)
    i = i - 1

# 3)print multiplication table for a user-specified number using a nested for loop
number=int(input("enter the number"))
for i in range(1,11):
    for j in range(1):
        print(f"{number}x{i}={number*i}")



# 4)uses "for" loop to find sum of all even numbers between 0 and 10 (inclusive)
sum=0
for i in range(0,11):
    if i%2==0:  #for odd (if i%2!=0)
        sum=sum+i
print("sum=",sum)

# 5):Calculate the sum of all numbers from 1 to a given number
n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum=",sum)

# 6):Display numbers from a list using loop
numbers=["suchi","ramu","pranav","mahi","sruthi"] 
for i in numbers:
    print(i)

# 7): Display numbers from -10 to -1 using for loop
for i in range(-10,-1):
    print(i)

# 8):Write a Python program to print the cube of all numbers from 1 to a given number
number=int(input("enter the number"))
for i in range(1,number):
   print(i, "Cube =", i**3)
