# quiz:
# What is the output of the following code?
#my_list = [10, 20, 30, 40, 50]
#print(my_list[1:4])
#[b] [10, 20, 30]

# Which method is used to add multiple elements to the end of a list?
#[c] extend()

# Consider the following list:
#fruits = ['apple', 'banana', 'orange']
#How can you remove 'banana' from the list?
#[a] fruits.remove('banana')

# What does the len() function return when applied to a list?
#[c] The number of elements in the list

#Which of the following list comprehensions generates a list of even numbers from 0 to 10
#[a] [x for x in range(11) if x % 2 == 0]


# Question 1):
#Reverse List:
#Write Python code to reverse the order of elements in the given list my_list .
#Print the reversed list.
my_list = [10, 20, 30, 40, 50, 11]
my_list.reverse()  # (or) print(my_list[::-1])
print(my_list)

# Question 2):
#Common Elements:
#Given two lists list1 and list2 , find and print the common elements between them
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = [x for x in list1 if x in list2]
print(common)

# Question 3):
#Unique Elements:
#Create a new list unique_list containing only the unique elements from the
#given list original_list . Print the unique list.
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(original_list))
print(unique_list)

# Question 4):
#Remove Duplicates:
#Remove duplicate elements from the given list duplicated_list and print the list
#without duplicates while preserving the order.
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
emptylist = []
for i in duplicated_list:
    if i not in emptylist:
        emptylist.append(i)
print(emptylist)



#Exercise 1: List Concatenation
#Write a Python script that concatenates two lists and prints the result
list1=[1,10,100,1000]
list2=[2,20,200,2000]
list3=[list1+list2]
print(list3)

#Exercise 2: List Repetition
#Write a Python script that repeats a list three times and prints the result
list = [1, 20, 300]
print(list * 3)

#Exercise 3: List Removal
#Write a Python script that removes the elements at even indices from a list
list = [1, 2, 3, 4, 5, 6]
result = [list[i] for i in range(len(list)) if i % 2 != 0]
print(result)

#Exercise 4: List Insertion
#Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list
list=[5,6,7,8,9]
list=[10,11,12]+list
print(list)

#List comprehensions

# 1. Square Numbers: Create a list of squares of numbers from 1 to 10.
list=[x**2 for x in range(1, 11)]
print(list)

# 2. Even Numbers: Generate a list of even numbers from 1 to 20
list=[x for x in range(1, 21) if x % 2 == 0]
print(list)

# 3. Words Lengths: Given a list of words, create a list containing the lengths of each word
words = ["apple", "banana", "cherry", "date"]
length=[len(word) for word in words]
print(length)