#print(range(0,10))

#print(tuple(range(0,15)))

#print(list(range(0,15)))

#print(list(range(0,10,3)))

''''for i in range(1,5):
    print(i,"hi")'''
    
    

'''for i in range(1,5,2):
    print(i,"hi")'''
'''    
l=[10,20,30,40,50]
for i in l:
    print(i)'''
    
'''l=[10,20,30,40]
for i in range(0,10):
    print(l)'''
    
'''l=[10,20,30,40,50]
s=0
for i in l:
    s=s+i
print("answer:",s)'''

# print numbers from 1 to 10
'''for i in range(0,11):
    print(i)'''
    
    
#print even numbers 2 to 20
'''for i in range(2,21,2):
    print(i,end=' ')
    '''
    
#print even or odd
'''n=int(input())
if n%2==0:
    print("even")
else:
    print("odd")
    '''
    
#sum of first 10 natural numbers
'''sum=0
for i in range(1,11):
    sum+=i
print(sum)'''

#string and print each char in a string
'''n=input('enter a string:')
for char in n:
    print(char,end=' ')'''
    
    
#multiplication
'''n=int(input("enter table number:"))
for i in range(1,11):
    print(n,'*',i,'=',n*i)    '''
    
# squares of numbers from 1 to 5
'''for i in range(1,6):
    print(i*i,end=' ')'''
    
#print elements of a list
'''num=[3,7,1,9,4]
for i in num:
    print(i)'''
    
#count vowels in a string
'''n=input()
vow="aeiouAEIOU"
count=0
for char in n:
    if char in vow:
       count+=1
print("no of vow:",count)'''

#factorial of number
'''n=int(input())
factorial=1    
for i in range(1,n+1):
    factorial*=i
print(f"factorial of a ss{n} is:",factorial)'''


print("==============================================================")


# while loops
'''i=1
while i<10:
    print("hi")
    i+=1'''

'''i=1
while i<10:
    print("hi")
    i=i+1'''

# print numbers from 1 to 10 using while loop
'''i=1
while i<=10:
    print(i)
    i+=1'''
    
#sum of 10 numbers
'''n=int(input())
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("sum:",sum)'''
  