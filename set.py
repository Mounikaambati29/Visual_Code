# Quiz

# Question 1:
# What is the output of the following code?
# my_set = {1, 2, 3, 4, 5}
# print(len(my_set))
# [b] 5

# Question 2:
# Which of the following methods is used to add an element to a set
# [a] add()

# Consider the following sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Which method would you use to find the elements that are common in both sets
# [a] intersection()

# Question 4:
# Which of the following statements about sets in Python is true
# [c] Sets are mutable

# Task 1: Set Intersection
# Write Python code to find and print the intersection of the following two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Output should be: {4, 5}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))
print(set2.intersection(set1))

#Task 2: Set Union
# Write Python code to find and print the union of the following two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Output should be: {1, 2, 3, 4, 5, 6, 7, 8}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set2.union(set1))

#Task 3: Set Difference
# Write Python code to find and print the elements present in set1 but not in set2:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Output should be: {1, 2, 3}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.difference(set2))
print(set2.difference(set1))

#Task 4: Set Symmetric Difference
# Write Python code to find and print the symmetric difference of the following two sets:
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# Output should be: {1, 2, 3, 6, 7, 8}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

#Task 5: Set Membership Test
# Write Python code to check if the element 3 is present in the set my_set :
# my_set = {1, 2, 3, 4, 5}
# Output should be: True

my_set = {1, 2, 3, 4, 5}
print(3 in my_set)

# Exercise 1: Set Intersection
# Write a Python script that finds and prints the intersection of two sets

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
set3=set1.intersection(set2) #(or)print(set1.intersection(set2))
print(set3)

# Exercise 2: Set Union
# Write a Python script that finds and prints the union of two sets

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
print(set1.union(set2))
print(set2.union(set1))

# Exercise 3: Set Difference
# Write a Python script that finds and prints the difference between two sets

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
print(set1.difference(set2))
print(set2.difference(set1))

# Exercise 4: Set Symmetric Difference
# Write a Python script that finds and prints the symmetric difference between two sets

set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))