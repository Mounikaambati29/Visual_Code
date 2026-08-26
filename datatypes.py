 #list
l=[1,2,3,4,6]
print(type(l))
l.append(5)  #append used to add some elements or characters
print(l)
l.extend([6,7,8])  #extend used to extend the list
print(l)
l.insert(8,9)      #insert used to add elements we have to give (index,element)
print(l)
l.remove(7)       #remove used to remove the elements from the list
print(l)          
l.pop()        #pop used to remove the last element from the list
print(l)
l.copy()        #copy used to copy the elemnts in the  list
print(l)
l.count(6)     #count used to count the elements in th list
print(l)
l.reverse()    #reverse is used to reverse the elements in the list
print(l)
l.sort()      #sort is used to arrange the elements in th ascending order
print(l)
l.clear()   #clear is used to clear the elements in the list
print(l)

#list inside list
nums=[11,'rushmi',33.5,[55,65.3,'chinni']]
print(nums)
print(type(nums))

#combining two lists into a single list
num1=[35,'deeshi,89.3']
num2=['ammu',68,22.5]
num3=[num1+num2]   #we can declare num1+num2 (or) num1,num2 
print(num3)

 #tuple
t=(3,66,'robin',89,85.5,32,'suma')
print(type(t))    #to identify the type

tup=(2,55,93,64,28)
print(min(tup))  #to identify the minimum element in the tuple
print(max(tup))   #to identify the maximum element in the tuple
print(len(tup))    #to identify the length of tuple

#set
#in set indexing and slicing are not possible
s={92,74,15,26,83,49}
print(type(s))  #to identify the type
print(s)
print(26 in s)    #check wheter the element in the set or not (True (or)False)
print(29 in s)    #check wheter the element in the set or not (True (or)False)

set1= set('abcdefg')
set2= set('aeiougd')
print(set2)
print(set1)
print(set1-set2)   #in set1&2 the common elements are removed and uncoomon in the set 1
print(set2-set1)   #in set1&2 the common elements are removed and uncoomon in the set 2 
print(set1&set2)   #it gives the output of common elements in the two sets
print(set1^set2)   #it gives the output of uncommon elements in the two sets
print(set1|set2)   #it gives all the elements in both two sets only once
#set methods
set1={81,'lose',116,25,'win',39,62}
set2={1,'profit',2,3,'gain',4,5}
set1.add(47)     #to add the elements in the set
print(set1)
print(len(set1))  #to measure the length of the seet
print(len(set2))
print(set1.update(set2))  #to update the set by another set 
print(set1)
print(set2.update(set1))
print(set2)
set1.remove(39) #to remove the element from the set(if the element is not found it will show error)
print(set1)
set2.discard('gain')   #to discard the element from the set(but here the error willnot be raise)
print(set2)
set2.discard(869)
print(set2)
set1.pop()
print(set1)
set2.pop()
print(set2)

s={1,5,3,9,8}
print(max(s))  #to identify the max element in the set
print(min(s))  #to identify th min element in the set
print(sum(s))  # the sum of the set
#operations in set
a={1,2,3,4,5,6,7}
b={1,2,3,4,5,6,7,8,9}
print(a.issubset(b)) #to identify seta elements are present in b(or)not
print(b.issubset(a)) #to identify setb elements are present in a(or)not
print(a.issuperset(b)) #to identify setb elements are present in a(or)not
print(b.issuperset(a)) #to identify seta elements are present in b(or)not
print(a.union(b)) #combining of two sets and common elements are written in 1time
print(b.union(a))
print(a.intersection(b))  #only common elements will return 
print(b.intersection(a))
print(a.difference(b))  #common elements deleted and uncommon elements will be written
print(b.difference(a))
print(a.symmetric_difference(b)) #uncommon elements will be written
print(b.symmetric_difference(a))
print(sorted(a))  #it arrange the elements in ascending order and it written as list
print(sorted(b)) 

#range
r=range(0,10)
print(type(r))
print(r)

#dictionary
d={}
print(type(d))
d={"a":1,"b":'rasi',"c":55.9}
print(type(d))
print(d)
print(d.copy())
print(d.get("a"))

#tuple-->list
tuple=("pythonlife",20.3,229,(297,"hani",1.2),[5,2,8],{6,52.7,8})
print(tuple)
print(type(tuple))
list=list(tuple)
print(list)
print(type(list))

#list-->set
list=[100,15.5,(15,"pythonlife",20.6),"hani"]
print(list)
print(type(list))
set=set(list)
print(set)
print(type(set))

#list-->tuple
list=[96,45.2,"mani",{"students":"teachers","age":"18"},93,62,83.4,[15,4]]
print(list)
print(type(list))
tuple=tuple(list)
print(tuple)
print(type(tuple))

# set-->list
set={96,45.2,"pythonlife",62,83.4,(15,4)}
print(set)
print(type(set))
list=list(set)
print(list)
print(type(list))