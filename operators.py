#task1
#Arithmetic operators
num1=8
num2=6
result=num1+num2
print(result)

num1=10
num2=5
result=num1-num2
print(result)

num1=8
num2=6
result=num1*num2
print(result)

num1=10
num2=5
result=num1/num2
print(result)

num1=20
num2=3
result=num1%num2
print(result)

num1=10
num2=2
result=num1**num2
print(result)

num1=20
num2=6
result=num1//num2
print(result)

#Assignment operators
num1 = 20
num2 = 4
num1 += num2  # equivalent to num1 = num1 + num2
print(num1)

num1=20
num2=4
num1 -= num2
print(num1)

num1=20
num2=4
num1 *= num2
print(num1)

num1=20
num2=4
num1 /= num2
print(num1)
num1=20
num2=4
num1 %= num2
print(num1)

num1=20
num2=4
num1 **= num2
print(num1)

num1=20
num2=4
num1 //= num2
print(num1)

#comparision operator
num1 = 50
num2 =50
result = num1 == num2
print(result)

num1 = 50
num2 = 50
result = num1 != num2
print(result)

num1 = 50
num2 = 50
result = num1 < num2
print(result)

num1=50
num2=50
result=num1 > num2
print(result)

num1=50
num2=50
result=num1<=num2
print(result)

num1=50
num2=50
result=num1>=num2
print(result)

#logical operator
num1=8
num2=4
result=num1 and num2
print(result)

num1=8
num2=4
result=num1 or num2
print(result)

num1=8
result=not num1
print(result)

#identify operator
num1 = 3
num2 = 3
result = num1 is num2   #for this the output will be false
result=num2 is num1     # for this the output will be true
print(result)               
print(result)              

num1 = 10
num2 = 5
result = num1 is not num2
print(result)

#membership data type
num1 = 10
num2 = [5, 10, 15]
result = num1 in num2
print(result)

num1 = 55
num2 = [2, 4, 6, 9, 10]
result = num1 not in num2
print(result)

#discount
price = 100
discount = 0.2
final_price = price - (price * discount)
print(final_price)
