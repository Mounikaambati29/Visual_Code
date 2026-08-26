# Quiz:   (task9)
# 1. What does the break statement do?
# [b] Exits the loop immediately

# 2. When is the continue statement used?
# [b]  To skip the rest of the code for the current iteration and move to the next

# 3.  What is the purpose of the pass statement?
# [c] Acts as a null operation, doing nothing

#Problem 1: Using break in a While Loop
#Write a Python program that takes a list of numbers as input numbers = [25,30,20,40,15,25]
#and prints the sum of the numbers. However, if the sum exceeds 100, 
#stop adding numbers and print "Sum exceeded 100".

# list = [25, 30, 20, 40, 15, 25]
# total=0
# i=0

# while i < len(list):
#     total = total +list[i]

#     if total > 100:
#         print("Sum exceeded 100")
#         break

#     i = i+1

# print("Sum:", total)

#Problem 2: Using continue in a For Loop
#Write a Python script that uses a for loop to iterate through numbers from 1 to 600
#Print only the odd numbers, skipping the even ones using the continue statement

# for i in range(1,601):
#     if i%2==0:
#         continue
#     print(i)


#Problem 3: Using pass in Conditional Statements
#Write a Python script that checks if a number is even or odd. If the number is
#even, print "Even"; if odd, do nothing (use the pass statement)

# number=int(input("enter a number:"))
# if number % 2 == 0:
#     print(f"The entered Number is Even: {number}")
# else:
#     pass

#Problem 4: Combining Transfer Statements
#Write a Python script that iterates through a list of words. If the word is "break," exit
#the loop using the break statement. If the word is "skip," skip the rest of the code for the
#current iteration using the continue statement. For any other word,print the word

words = ["nani", "chinni", "manu", "break", "lilly", "sanju", "skip","bhuvan"]
for i in words:
    if i == "break": #if we give break before skip means it will print only before break words.
        break

    if i== "skip":   #if we give skip before break means it will print upto bhuvan
        continue
    print(f"Print the i: {i}")



