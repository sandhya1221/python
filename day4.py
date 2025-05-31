#sum of given integer
'''def fun(n):
    if n==0: return 0
    return 1+fun(n//10)
print(fun(1234))'''

#sum of digits
'''def fun(n):
    if n//10==0: return 1
    return 1+fun(n//10)
print(fun(1234))
'''

#recurssion
'''def fun(n):
    if n//10==0: return n
    return n%10+fun(n//10)
print(fun(157))'''


#minmax value using recursion
'''def minmax(arr,n):
    if n==1:
        return arr[0],arr[0]
    else:
        min_val,max_val=minmax(arr,n-1)
        return min(arr[n-1],min_val),max(arr[n-1],max_val)
arr=[1,5,3,7,33]
n=len(arr)
print(minmax(arr,n))'''

# find the middle element
'''def mid(lst, start, end):
    if start == end:
        return lst[start]
    return mid(lst, start + 1, end - 1)
n = [1, 2, 3, 4, 5]
middle_element = mid(n,0,len(n)-1)
print("Middle element is:", middle_element)'''

# slow fast
'''l=[7,5,4,1,3]
slow=0
fast=0
while fast<len(l)-1 and fast+1<len(l):
    slow+=1
    fast+=2
print(l[slow])    '''

#palindrome
'''def palindrome(n):
    return str(n)==str(n)[::-1]
n=input()
if palindrome(n):
    print("palindrome")
else:
    print("not a palindrome")'''

    
    
   
        







    
 





    
    
    
        
        
        

    
    