#decimal to binary
'''a=8
print(bin(a))'''


'''a=8
if 6:
    print("hi")'''
    
'''a=8
rem=""
while a:
    rem+=str(a%2)
    a=a//2
print(rem[::-1])'''


#modules
'''a=3%2
print(a)'''


#binary to decimal
'''a="101"
a=a[::-1]
dec=0
for i in range(len(a)):
    dec+=int(a[i])*(2**i)
print(dec)'''


#decimal to binary 
'''a=10
rem=""
while a:
    rem+=str(a&1)
    a=a>>1
print(rem[::-1])'''



# count no of bits  ex if 2-01,4-1000
'''a=2
count=0
while a:
    a=a>>1
    count+=1
print(count)'''

#count the nof ones in binary
'''a=2
count=0
while a:
    if a&1==1:
        count+=1
    a=a>>1
print(count)'''

# count no of zeros in binary
'''a=10
count=0
while a:
    if a&1==0:
        count+=1
    a=a>>1
print(count)'''


#find 1st set bit from right side
'''n = 18 
position = 0

while (n & 1) == 0:
    n = n >> 1
    position += 1

print(position)
'''

'''n= 5
position = 0

while (n & 1) == 0:
    n = n << 1
    position -= 1

print(position)'''

# find 1st set bit from left side
'''a=9
pos=-1
while a >1:
    a=a>>1
    pos+=1
print(pos)  '''


# clearing the ith position ,,,check ith bit of binary number it is 1 replace it with 0 or if it is 0 dont change the number and print the binary num as it is
'''def clear(a,i):
    mask=1<<i
    mask=~mask
    return a & mask
print(clear(8,3)) '''


#set 1 in ith bit 
'''def fun(a,i):
    mask=1<<i
    return a|mask
print(fun(8,2))

'''
#get the ith position bit 
'''def pos(a,i):
    mask=1<<i
    return 1 if mask&a>0 else 0
print(pos(8,2))'''


#check the number is power of 2
'''def square(a):
    return (a&(a-1))==0
print(square(4))'''

'''
a=[1,2,2,3,4,3,4,1,9]
res=0
for i in a:
    res^=i
print(res)'''


#odd no of duplicates(Assessment)


#recurrsion(count the digits in a integer value)
'''def fun(n):
    if n:
        fun(n-1)
        return n
print(fun(5))'''



#infinite loop AND some errors
'''def fun(n):
    print(n)
    fun(n-1)
print(fun(5))
 '''

    
    
#recurrsion(count the digits in a integer value)
'''n=123
count=0
if n==0:
    count=1
else:
    while n>0:
        count+=1
        n=n//10
print("digits:",count)'''



''''def fun(n):
    if n==0: return
    print(n,end=" ")
    fun(n-1)
    print(n,end=" ")
print(fun(5))'''
'''
def fun(n):
    if n:
        fun(n-1)
        return n
print(fun(5))'''


#recursion(error)
'''def fun(n):
    if n==1 or n==0: return 1
    fun(n-1)
    print(n)
    fun(n-3)
print(fun(5))'''


#ASSESSMENT BINARY TO DECIMAL
'''n='1011'
dec=0
pow=0
n=n[::-1]
for i in n:
    dec+=int(i)*(2**pow)
    pow+=1
print(dec)'''


#check the number is even or odd
'''a=3
if a&1==0:
    print("even")
else:
    print("odd")'''
    
    
# swap the numbers using xor
'''a=10
b=5
a=a^b
b=a^b
a=a^b
print("after swapping {a}:",a)
print("after swapping {b}:",b)'''


# count the no of 1's
'''a=15
count=0
while a:
    if a&0==0:
        count+=1
    a=a>>1
print(count)'''


# add two integers without using '+' and '-'

a=10
b=5
while b!=0:
    carry=a&b
    a=a^b
    b=carry>>1
print(a)  
        