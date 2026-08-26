#Quiz answers (day four tasks)
# 1) What do identity operators (is, is not) check in Python?
#  [b] memory address identity

# 2) which statement is correct for the identity operator is?
#  [b] x is y is True if x and y refer to the same object.

# 3) What do membership operators (in, not in) check in Python?
#  [d] Sequence membership

# 4) Which membership operator checks if a value is not present in a sequence?
#  [b] not in

# Exercise :
#1)Takes user input for their name & age use (f-strings) to print a message
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Welcome {name}!")
print(f"You are {age} years old.")

# 2)List and Membership Operators
numbers = [42, 22, 89, 91, 53, 26, 79, 18, 99, 120]
print(26 in numbers)
print(82 not in numbers)

#  Quiz Answers

#1) x = 15
# y = 4
# result = x // y
# [b] 3

# 2)a = 7
# b = 3
# c = a % b
# print(c)
# [a]1

#3) Which assignment operator is equivalent to x = x + 5?
# [a] x += 5


#4) What is the result of 5 < 10 and 10 > 7?
# [a] True


#5) If x = True and y = False, what is the value of not x or y?
# [b] False

#Exercise 1:Area of a Rectangle using the given formula:area=length*width values of length& width as inputs from the user
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print ("area of rectangle ",  area)

#Exercise 2:To demonstrate Incrementing and Decrementing a Variable
num1 =15+1   #Increment
num2 =15-1   #Decrement
print(num1)
print(num2)

#excercise 3:To convert temperature from Celsius to Fahrenheit formula is:F=(C*9/5)+32 inputs from the user
celsius = float(input("enter the temperature in celsius: "))
f = (celsius * 9/5) + 32
print ("temperature in fahrenheit: ", f)

#excercise 4:To calculate the simple interest given the principal amount,rate&time (in years)
principal = int(input("enter principal amount: ")) #here we can give either int(or)float
rate = int(input ("enter rate :"))
time = int(input("time in years: "))
si = (principal * rate * time / 100)
print ("simple interest: ", si)

#excercise 5:To concatenate two strings & display the result.strings taken as input from the user
name1 = str(input("enter string1 "))
name2 = str(input("enter string2 "))
result = name1+name2
print("concatenated string: " , result)

# excercise 6:To convert a distance from kilometers to miles
kilometer = int(input("enter the distance in kilometers : ")) #here we can give either int(or)float
miles = kilometer * 0.621371
print ("distance in miles: " , miles)
