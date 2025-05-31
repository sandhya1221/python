#Prime num
#Easy approach(we can print the num)
'''n=int(input())
for i in range(1,n+1):
    if(n%i==0):
        print(i)'''   #OUTPUT:5,  1 5
    
        
# count the primes with out printing all the nums
'''n=int(input())
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count==2):
    print("prime nums:",count)
else:
    print("not prime:",count)'''    #OUTPUT: 5, prime:2

        
        
# print prime or not     
'''n=int(input())
if n<=1:
    print("not prime")
elif n==2:
    print("prime")
elif n%2==0:
    print("not prime")
else:
    print("prime")'''  #OUTPUT: 5 , prime
    
#Method t use in  interviews
#Sieve of Erotheneses
'''n=int(input())
arr=[1]*n
for i in range(2,int(n**0.5)+1):
    if arr[i]==1:
        for j in range(i*i,n,i):
            arr[j]=0
count=0
for i in range(2,n):
    if arr[i]==1:
        count+=1
print(count) '''  #OUTPUT: 5, 2  TC:O(n log log n)==>O(1)     SC:O(n)
'''==========================================================================================='''
    
#reverese a string
'''n=input()
rev=n[::-1]
print("reversed string:",rev)'''

'''==========================================================================================='''

#palindrome or not
'''def palindrome(n):
    return str(n)==str(n)[::-1]
n=input()
if palindrome(n):
    print("palindrome")
else:
    print("not a palindrome")'''
    
'''==========================================================================================='''
    
#find the fst non repeating character in string
'''n=input()
frequency=0
for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
    if count==1:
        print(" first non repeating:",i)
        frequency=1
        break
else:
    print(" non repeting")'''
    
'''==========================================================================================='''
    
#count no of vowels and cnsonants
'''n=input()
vow="aeiouAEIOU"
vow_count=0
con_count=0
for char in n:
    if char in vow:
       vow_count+=1
    else:
        con_count+=1
print("vowels:",vow_count)
print("consonants:",con_count)
'''

'''==========================================================================================='''

#remove duplicates
'''n=input()
res=[]
count=0
for char in n:
    if char not in res:
        res.append(char)
for char in res:
    print(char,end="")'''


'''==========================================================================================='''

#pyramid
'''for i in range(6):
    for j in range(i):
        print("*",end=' ')
    print()'''
    
#reverse pyramid
'''for i in range(6):
    for j in range(6-i):
        print("*",end=" ")
    print()'''
    
# tree like pattern
'''for i in range(5):
    for k in range(5-i):
        print('',end=' ')
    for j in range(i):
       print("*",end=' ')
    print()'''
    
# combinin the two patterns
'''for i in range(5):
    for j in range(i):
        print("*",end='  ')
    print()
for i in range(5):
    for j in range(5-i):
        print("*",end='  ')
    print()'''
    
'''==========================================================================================='''
        
#print(2**3)
#print(8**2)
'''print(3**2)
print(2**9)'''

'''==========================================================================================='''

#reverse string with constraints
'''def revese(x):
    rev=0
    if x < 0:
        rev=int(str(x)[1:][::-1])*-1
    else:
        rev=int(str(x)[::-1])
    if rev > 2**31-1 or rev < -2**31:
        return 0
    return rev
x=-123
print(revese(x))'''

'''==========================================================================================='''

#count the no of vowels
#Basic problem soliving
'''n=input()
s=n.lower()
a=s.count("a")
e=s.count("e")
i=s.count("i")
o=s.count("o")
u=s.count("u")
print(f"no ot vowels:{a+e+i+o+u}")'''

#usinf for loops
'''n=input()
vow="aeiouAEIOU"
count=0
for char in n:
    if char in vow:
        count+=1
print("no of vowels:",count)'''


'''==========================================================================================='''


#calcluate the total marks and avg marks and grade
'''m=int(input("marks in maths:"))
s=int(input("marks in science:"))
e=int(input("marks in englsh:"))
total_marks=m+s+e
avg_marks=total_marks/3
percentage=(total_marks/300)*100
Grade=""
if percentage>90:
    Grade="A"
elif percentage>80:
    Grade="B"
elif percentage>70:
    Grade="C"
else:
    Grade="Fail"
  
print("total_marks:",total_marks)
print("avg_marks:",avg_marks)
print("Grade:",Grade)'''


'''==========================================================================================='''

#PALINDROME
'''n=(input())
if str(n)==str(n)[::-1]:
    print("it is a palindrome")
else:
    print("not palindrome")'''
    
#Method 2
def isPalindrome(n):
    return str(n)==str(n)[::-1]
n=input()
if isPalindrome(n):
    print("palindrome")
else:
    print("not palindrome")

#METHOD 3
'''n=input("Give a string:")
rev=n[::-1]
if rev==n:
    print("palindorme")
else:
    print("not palindrome")'''
    
    
'''==========================================================================================='''
    
#Largets number among three numbers
'''a=int(input("enter a num:"))
b=int(input("enter a num:"))
c=int(input("enter a num:"))
if a>b and a>c:
    print("largest num:",a)
elif b>a and b>c:
    print("largets num:",b)
else:
    print("largest num:",c)'''
    

#METHOD 2
'''a=15
b=8
c=21
if a>b and a>c:
    print("largest num:",a)
elif b>a and b>c:
    print("largets num:",b)
else:
    print("largest num:",c)'''
    
#METHOD 3
'''n=input()
x,y,z=n.split(",")
a=int(x)
b=int(z)
c=int(x)

if a>b and a>c:
    print("largest num:",a)
elif b>a and b>c:
    print("largets num:",b)
else:
    print("largest num:",c)'''
    
'''==========================================================================================='''
    
#LEAP YEAR or not
'''n=int(input("enter a year:"))
if (n%4==0 and n%100!=0) or(n%400==0):
    print("it is a leap year")
else:
    print("it is not a  leap year")'''
    
'''==========================================================================================='''

#While loop
'''i = 0
while i < 3:
    print(i)
    i += 1'''

#EXAMPLE 2
'''candies=10
while candies<0:
    print("given to friend")
candies-=1
print(candies)'''

'''==========================================================================================='''

#For loop
'''candy=10
for i in range(0,10):
    print("candy given to frnd")'''
    
#For loop for sequence
'''l=[1,2,3,5,6]
for i in l:
    print(i,end=" ")'''
    
#method 2
'''message="Hello world"
for char in message:
    print(char)'''
#method 3
'''for i in range(0,5):
    print("hi")'''

#NESTED LOOP(Multiplication table)
'''for i in range(1,6):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")'''

#Break
'''candies=10
for i in range(0,11):
    print("giving to frnd")
    if candies -i==6:
        print("only 5 left stop")
        break
'''

#CONTINUE
'''candies=10
for i in range(candies):
    print("giving to frnd")
    if candies-i==5:
        print("ti is spcl")
        continue'''
        
        
#PROGRAMS (print all the nums from 1 to n)
# USING FOR LOOPS
'''n=int(input()) 
for i in range(1,n):
    print(i)'''
    
'''n=6
for i in range(1,6):
    print(i)'''
    
#USING WHILE LOOP:
'''n=1
while n<=5:
    print(n)
    n+=1'''
 
#sum of fst natural numbers
'''n=5
sum=0
for i in range(1,6):
    sum+=i
print("sum of first natural num:",sum)'''

#while loop
'''n=1
sum=0
while n<=5:
    sum+=n
    n+=1
print("sum of natural nums:",sum)'''

#print even num
'''n=10
for i in range(2,11,2):
    print(i)'''

#while loop
'''n=2
while n<=10:
    print(n)
    n+=2'''
    
#MULTIPLICATION OF TABLES
#USING FOR LOOP

'''i=3
for j in range(1,11):
    print(f"{i}*{j}={i*j}")'''
    
#while loop
'''i=3
j=1
while j<=10:
    print(f"{i}*{j}={i*j}")
    j+=1'''
    
#calculate the factorial of num
'''n=5
fact=1
for i in range(1,6):
    fact*=i
    print("factorial is:",fact)'''
    
#while
'''n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial:",fact)'''

#FUNCTIONS  (sum of two num)
'''def sum(a,b):  #defining function
    print(a+b)
sum(5,10)   '''  #calling function


#keyword arguments(Using function)
'''def fun(name,age):
    print("Name:",name)
    print("age:",age)
result=fun(age=30,name="abcd")'''

#Default arguments
'''def default(name,greeting="hii"):
    return greeting+" , "+name+" "
greeting1=default("Bob")
greeting2=default("charlie","hello")
print(greeting1)
print(greeting2)'''

#Accessing the scope of variables
#GLOBAL VARIABLES:ti is defined outside the function can be accessible from anywhere in the code
'''global_var=10  #the var name should not be only global_var it can be anything
def fun():
    print(global_var)  #access from any where like out of the fun or inside the fun
print(global_var)'''


#LOCAL VARIABLES:it is defined inside the function and only accessible within the function
'''def my_fun():
    local_var=6
    print(local_var)
my_fun()'''

#LAMBDA function (SYNTAX -- lambda arguments:expression)
'''add=lambda x,y:x+y
result=add(3,4)
print(result)'''

#finding the sum of 2 numbers using functions:
'''def fun(a,b):
    return a+b

result=fun(3,2)
print("sum of two nums:",result)'''


#area of circle
'''def area(r):
    return 3.14*(r**2)  #pie r**2
result=area(5)
print(result)'''

#swapping without temp and using functions
'''def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b
a=10
b=20
a,b=swap(a,b)
print("after swapping:",a)
print("after swapping:",b)'''

#without functions 
'''a=int(input())
b=int(input())
a,b=b,a
print(a)
print(b)'''

    
#using functions leetcode subset problem (without using class solution)----using take and no take
'''def generate(ind,curr,ans,nums):
    if (ind==len(nums)):
        ans.append(curr.copy())
        return
    curr.append(nums[ind])
    generate(ind+1,curr,ans,nums)
    curr.pop()
    generate(ind+1,curr,ans,nums)
def subset(nums):
    ans=[]
    generate(0,[],ans,nums)
    return ans
nums=[1,2,3]
print(subset(nums))'''


#practice simple merge algorith
'''n1=list(map(int,input().split()))
n2=list(map(int,input().split()))
i=0
j=0
result=[]
while i<len(n1) and j<len(n2):
    if(n1[i]<=n2[j]):
        result.append(n1[i])     
        i+=1
    else:
        result.append(n2[j])     
        j+=1
while(i<len(n1)):
    result.append(n1[i])
    i+=1
while(j<len(n2)):
    result.append(n2[j])
    j+=1
print(result)'''


#EVEN NUMBER USING FILTER METHOD
'''
def is_even(num):
    return num % 2 == 0 

numbers=[1,2,3,4,5,6]
filtered = filter(is_even, numbers)
print(list(filtered))'''

#LIST :it is mutable(it can  be changeable)
#denoted by []
# in list if we want to add anything we use (.append)

#TUPLE:it is immutable(it cant be changed after the tuple creation)
#denoted by ()
#once tuple is created we cant add,remove,modify the elements in tuple
#CREATION OF TUPLE
'''my_tuple=(1,2,3,4)
print(my_tuple)'''

#Accessing the tuple : u can access the values in a dict using square brackets [] with the key
'''tuple=(1,2,3,4)
print(tuple[0])'''

#using slicing
'''tuple=(1,2,3,4)
print(tuple[0:3])'''


#methods in tuple are limited bcoz of their immutability
#we use index() and count()
#example count
'''tuple=(2,3,4,4,1)
count=tuple.count(4)
print(count)'''

#example index  it eill return the index values
'''tuple=(1,2,3,4)
index=tuple.index(4)
print(index)   OUTPUT: 2'''

#SET:set in python is unorderd colection og unique elements and it is defined by {}
# it is mutable(change)
# it automatically removes the duplicate values
#in sets to add anything to the existing one we can use (.add)

#creating empty set
'''my_set=set()'''
#creating a set with elements
'''fruits={'apple','banana','cherry'}
print(fruits)'''

#creating a set from  a list
'''num=set([1,2,3,4,5])
print(num)''' #here list is converted to set

'''num=set((1,2,3,4,5))
print(num)'''  #here tuple is converted to set

#Adding elemets to set
'''set={1,2,3}
set.add(5)
print(set)'''

#Removing elements from set
'''set={1,2,3}
set.remove(2)
print(set)'''

#SET operations
#UNION
'''s1={1,2,3}
s2={2,5,6,7}
s1=s1.union(s2)
print(s1)'''

#INTERSECTION(same elements should be printed)
'''s1={1,2,3}
s2={2,5,6,7}
s1=s1.intersection(s2)
print(s1)  OUTPUT: 2'''


#DIFFERENCE
'''s1={1,2,3,4}
s2={1,2,7,8,9}
s3=s1-s2
print(s3)'''
#for the above example s1 values should b printed bcoz dubtracting from the s1

#set MEMBERSHIP and LENGHT operation
'''set={1,2,3,4}
print(2 in set)
print(7 not in set)''' #OUTPUT:True True

#length
'''set={1,2,3,4}
print(len(set))''' #OUTPUT:4

'''set={'a','b','c'}
print(len(set))'''  #OUTPUT:3

#set methds
#clear(),update(),copy(),pop()
'''set={1,2,3}
set.clear()
print(set)'''

#copy
'''set={1,2,3}
set.copy()
print(set)'''


#DICTIONARY:Dictionary is an unordered collection of key value pairs are usted to store the data in the form of key valyes
#{}
''''my_dict={'name':'sandhya','age':'abd'}
print(my_dict)'''

#Accesssing the dict
'''my_dict={'name':'sandhya','age':'abd'}
print(my_dict['name'])'''

#Add the new key to the list
'''my_dict={'name':'sandhya','age':'abd'}
my_dict['address']='hyd'
print(my_dict)'''

#loops
'''my_dict={'name':'sandhya','age':'abd'}
for key in my_dict:
    print(key)'''

#need to display both key and values
'''my_dict={'name':'sandhya','age':'abd'}
for key,value in my_dict.items():
    print(key,value)'''

           
    
    
    
    
    

    