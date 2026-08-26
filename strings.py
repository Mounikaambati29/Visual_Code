# Quiz
#What is the main characteristic of Python strings?
#[b] Immutable

#How can you access the last character of a string in Python?
#[a] my_string[-1]

#Which method is used to convert a string to uppercase in Python?
#[c] .upper()

#What does the split() method do?
#[b] Splits a string into a list of substrings

#Which method is used to check if a string starts with a specific prefix?
#[a] startswith()

#Problem 1:
#You are given a string sentence . Print the characters at even indices.
# Example: sentence = "Python is amazing"
# Output: "Pto saaig 

str = "python is amazing"
result = ""
for i in range(0,len(str),2):
    result = result +str[i]
print(f'"{result}"')

#problem 2:
#You are given a string s . Replace all spaces in the string with underscores ( _ )
#and print the modified string.
# Example: s = "Python is fun and powerful"
# Output: "Python_is_fun_and_powerful"

str="python is fun and powerful"
result=str.replace(" ","_")
print(result)

#problem 3:
#You are given a string s . Check if the string contains only digits.
# Example: s = "12345"

str="12345"
result=str.isdigit()
print(result)

#problem 4:
#You are given a string s . Print the string in reverse order.
# Example: s = "Python is amazing"
# Output: "gnizama si nohtyP

str="python is amazing"
print(str[::-1])

#problem 5:
#You are given a string s . Capitalize the first letter of each word in the string
#and print the modified string.
# Example: s = "python programming is fun"
# Output: "Python Programming Is Fun"

str = "Python programming is fun"
str1 = str.split()
for i in range(len(str1)):
    str1[i] = str1[i].capitalize()
    result = " ".join(str1)
print(result)  