#Quiz
# Question 1:
# What is the output of the following code?
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(len(my_dict))
# [c] 3

# Question 2:
# Which method is used to add a new key-value pair to a dictionary?
# [d] update()

#   Question 3:
#Consider the following dictionary:
#my_dict = {'name': 'python', 'age': 30, 'city': 'Tadepalligudem'}
#How can you access the value associated with the key 'age'?
#[a] my_dict.get('age')

#  Question 4:
#What happens if you try to access a key that doesn't exist in a dictionary using
#square brackets notation?
#[b] It raises a KeyError.

#Question 5:
#Which of the following methods returns a list of all the keys in a dictionary?
#[d]  list_keys()

# Task 1: Dictionary Update
# Write Python code to add a new key-value pair to the following dictionary:
# my_dict = {'name': 'python', 'age': 25}
# Output should be: {'name': 'python', 'age': 25, 'city': 'west godavari"}
my_dict = {'name': 'python', 'age': 25}
my_dict['city'] = 'chennai'
print(my_dict)

#Task 2: Dictionary Access
# Write Python code to access and print the value associated with the key 'price' in
# the following dictionary:
# product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
# Output should be: 1200
product_info={'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info['price'])

#Task 3: Dictionary Removal
# Write Python code to remove the key-value pair with the key 'city' from the following dictionary
# my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
# Output should be: {'name': 'John', 'age': 30}
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
del my_dict["city"]
print(my_dict)

#Task 4: Dictionary Keys
# Write Python code to print all the keys present in the following dictionary:
# my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
# Output should be: ['name', 'age', 'city']
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(list(my_dict.keys()))

# Task 5: Dictionary Values
# Write Python code to print all the values present in the following dictionary:
# my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
# Output should be: ['python', 25, 'tanuku']
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(list(my_dict.values()))


#Exercise 1: Dictionary Update
#Write a Python script that updates a dictionary with a new key-value pair.
my_dict={'name':'python','age':25,'city':'vizag'}
my_dict.update({'country':'India'})
print(my_dict)

# Exercise 2: Dictionary Access
# Write a Python script that accesses and prints the value associated with a specific
# key in a dictionary
my_dict={'name':'python','age':25,'city':'vizag'}
print(my_dict['city'])

# Exercise 3: Dictionary Removal
# Write a Python script that removes a key-value pair from a dictionary
my_dict={'name':'python','age':25,'city':'vizag'}
del my_dict['name']
print(my_dict)

# Exercise 4: Dictionary Keys
# Write a Python script that prints all the keys present in a dictionary
my_dict={'name':'python','age':25,'city':'vizag'}
print(my_dict.keys()) #(or) we can write print(list(my_dict.keys()))

# Exercise 5: Dictionary Values
# Write a Python script that prints all the values present in a dictionary
my_dict={'name':'python','age':25,'city':'vizag'}
print(my_dict.values())