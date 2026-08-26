#Quiz:(day 5 task)
#1) Indentation is crucial in Python to
#   [D] Define the code of a code  block
#2) What will be the output of the following code
#   [A] Greater than 5
#3) In the if-elif-else statement, how many conditions can be checked
#   [c]multiple
#4) In the if-elif-else statement, how many conditions can be checked
#   [B]To provide an alternative block of code when te if condition is false
#5) Which of the following statements is true about a nested if statement
#   [B]It allows for more complex conditional logic

#Exercises:
#1)  character as input & checks whether it is a vowel(or)not. Use the if-else statement
c=input("enter a character:")
vowel="aeiouAEIOU"
if c in vowel:
    print(f"it is a vowel")   #without f-string also it will work
else:
    print(f"it is not a vowel") 


#2)  Age as input and classifies the person into one of the following age groups:
age=int(input("enter the age:"))
if age>0 and age<12:
    print("child")
elif age>13 and age<17:
    print("teenager")
elif age>18 and age<64:
    print("Adult")
elif age>+65:
    print("senior")
else:
    print("invalid age")


#3)  An integer as input and classifies it as positive,negative,(or)zero
num=int(input("enter a integer:"))
if num>0:
    print("it is positive")
elif num<0:
    print("it is negative")
else:
    print("it is zero")

 
#4)   checks whether a given year is a leap year or not.
#A leap year is divisible by 4, but not by 100 unless it is divisible by 400.
year=int(input("Enter a year:"))
if (year%4==0 and year%100 !=0) or (year % 400==0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#5)   Takes two numbers & an operator (+,-,*,/) as input & performs corresponding operation
num1=int(input("enter a number"))
num2=float(input("enter a number"))
operator=input("enter a operator(+,-,*,/)")
if operator=="+":
    print(num1+num2) #we can write "result:",num1+num2
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print("invalid")

#6)  Rewrite the following code using the short-hand
#if x % 2 == 0: result = "Even"
# else: result = "Odd"
x=8
result="even" if x%2==0 else "odd"
print(result)

#7)  calculates the final price after applying a discount.
#The program should take the original price and the discount percentage as input
originalprice = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))
finalprice = originalprice - (originalprice * discount / 100)
print("finalPrice:",finalprice)

#8)  calculates BodyMass Index(BMI) using the formula:BMI=weight(kg)/(height (m))^2
#weight and height as input
weight=int(input("enter the weight(kg):"))
height=int(input("enter the height(m):"))
bmi=weight/(height**2)
print("BMI =", bmi)
