# find the unique value in the list 11223
# prime numbers or not
# count the vowels in the string


#counting the vowels
'''def countvow(s):
    vow="aeiouAEIOU"
    count=0
    for char in s:
        if char in vow:
            count+=1
    return count
s=input()
print(countvow(s))'''
    




#prime numbers
'''n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
    else:
            print("Prime number")'''

#unique elements
'''
list=[1,1,2,2,3]
unique = []

for i in list:
    if list.count(i) == 1:
        unique.append(i)

print("Unique values:", unique)'''

'''
s=input()
def sum(s):
    total=0
    for i in range(1,len(s)+1):
        total+=1
    return total
print(sum(s))'''

'''
s="abcd"
sum=0
for i in s:
    sum+=ord(i)-96'''
    
    
#converting lower value(vowels)in to upper
''''s = "abceik"
vowels = "aeiou"
for ch in s:
    if ch in vowels:
        print(chr(ord(ch)-32),end="")  
    else:
        print(ch,end="")''''
        
        
        
s = "abcdEFGH"
for ch in s:
    print(chr(ord(ch)-32),end="")  
    else:
        print(ord(ch)+32,end="")
        
        
        


        



    
    
    
    


