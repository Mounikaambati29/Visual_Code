# Quiz

# Question 1:
# What is the purpose of using functions in Python
#a) To organize code into logical blocks
#b) To improve code readability and maintainability
#c) To enable code reuse
#d) All of the above
# Ans: [d] All of the above

# Question 2:
# Which keyword is used to define a function in Python
#[a] def

# Question 3:
# Which of the following is a valid way to call a function named my_function with
# no arguments in Python
#[a] my_function()

# Question 4:
# What is the scope of a variable defined inside a function in Python
#[a] Local scope

# Task 1: Add Function
# Write a Python function named add that takes two arguments a and b and returns their sum
def add(a,b):
    print(a+b)
add(81,90)

# Task 2: Square Function
# Write a Python function named square that takes a number x as input and returns its square
def square(a):
    result = a**2
    print(result)
square(5) 

# Task 3: Factorial Function
# Write a Python function named factorial that takes a positive integer n as
# input and returns its factorial
import math
def factorial(n):
    result = math.factorial(n)
    print(result)
factorial(5)    

# Task 4: Maximum Function
# Write a Python function named maximum that takes a list of numbers as input and
# returns the maximum value in the list
def maximum(x):
    max_value = max(x)
    print(max_value)
maximum([81,90,79,14,62,49,38,60,42,33])  

# Task 5: Reverse Function
# Write a Python function named reverse that takes a string s as input and
# returns its reverse
def reverse(*x):
    reverse_str= x[::-1]
    print(reverse_str)
reverse('apple','mango','pineapple','banana','jackfruit','orange')

# Task 6: Check Prime Function
# Write a Python function named is_prime that takes a positive integer n as input
# and returns True if n is prime, otherwise False
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print('not prime')
                break
        else:
            print('prime')
    else:
        print('Given input is not prime')            
prime(23)

# Task 7: Fibonacci Function
# Write a Python function named fibonacci that takes a positive integer n as
# input and returns the n th Fibonacci number
def fibonacci(a):
    if a>1:
            num = (a-1)+(a-2)
            print(num)
    else:
            print('Given num is wrong')
fibonacci(22)

# Task 8: Palindrome Function
# Write a Python function named is_palindrome that takes a string s as input and
# returns True if s is a palindrome, otherwise False
def palindrome(x):
    if x==(x[::-1]):
      print("palindrome")
      print(True)
    else:
        print("not a palindrome")
        print(False) 
palindrome("999")    

# Task 9: Sum of Squares Function
# Write a Python function named sum_of_squares that tmbersakes a list of numbers as
# input and returns the sum of the squares of those numbers
def sum_of_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum+= i**2
        print(f"sum of squares {sum}")
    else:
       print("not found")
sum_of_squares(4)            

# Task 10: Average Function
# Write a Python function named average that takes a list of numbers as input and
# returns the average value
def average(numbers):
    return sum(numbers)/len(numbers)
print(average([9,1,6,4,8]))
