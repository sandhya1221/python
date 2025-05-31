#single among doubles in gfg  (done in leetcode)
'''def search(arr,n):
    n=len(arr)
    if(n==1):
        return arr[0]
    if(arr[0]!=arr[1]):
        return arr[0]
    elif(arr[n-1]!=arr[n-2]):
        return arr[n-1]
    low=1
    high=n-2
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]):
            return arr[mid]
        elif((mid%2==1 and arr[mid]==arr[mid-1]) or mid%2==0 and arr[mid]==arr[mid+1]):
            low=mid+1
            #you ar on right half
        elif((mid%2==0 and arr[mid]==arr[mid-1]) or mid%2==1 and arr[mid]==arr[mid+1]):
            high=mid-1
n=5
arr=[1,2,2,5,5]
print(search(arr,n))'''

'''=========================================================================='''

#square root in gfg (using binary search)
'''def sqrt(n):
    low=1
    high=n
    ans=0
    while(low<=high):
        mid=(low+high)//2
        if(mid*mid<=n):
            ans=mid
            low=mid+1
        elif(mid*mid>n):
            high=mid-1
    return ans
n=4
print(sqrt(n))'''
#method 2
'''def floorSqrt(n):
    for i in range(1, n + 1):
        if i * i > n:
            return i - 1
    return n'''

'''=========================================================='''

#nth root
'''def cube(n,m):
    ans=-1
    for i in range(1,m+1):
        if(i**n==m):
            ans=i
            break
        elif(i**n>m):
            break
    return ans
n=3
m=27
print(cube(n,m))'''

#nth root using binary search
'''def nthroot(n,m):
    low=1
    high=m
    while(low<=high):
        mid=(low+high)//2
        if(mid**n==m):
            return mid
        elif(mid**n>m):
            high=mid-1
        elif(mid**n<=m):
            low=mid+1
    return -1
n=3
m=9
print(nthroot(n,m))'''

'''============================================='''

#smallest divisor(using linear search)(nt optimal)
'''from math import*
def smallestDivisor(arr,k):
    for div in range(1,max(arr)+1):
        Sum=0
        for num in arr:
            Sum+=ceil(num/div)
        if(Sum<=k):
            return div
arr=[1,2,5,9]
k=6
print(smallestDivisor(arr,k))'''

#smallest divisor using binary search(in gfg)
from math import*
'''def smallestDivisor(self, arr, k):
    low=1
    high=max(arr)+1
    while(low<=high):
        div=(low+high)//2
        Sum=0
        for num in arr:
            Sum+=ceil(num/div)
            if(Sum<=k):
                high=div-1
            else:
                low=div+1
    return low
arr=[1,2,5,9]
k=6
print(smallestDivisor(arr,k))  '''

'''============================================================='''

#koko eat banana(gfg)
#linear search
'''from math import*
def kokoeatBanana(arr,k):
    for banana in range(1,max(arr)):
        time=0
        for num in arr:
            time+=ceil(num/banana)
        if(time<=k):
            return banana
arr=[3,6,7,11]
k=8
print(kokoeatBanana(arr,k))'''

#Using Binary search
'''from math import *
def kokoeatBanana(arr,k):
    low=1
    high=max(arr)
    while(low<=high):
        banana=(low+high)//2
        time=0
        for num in arr:
            time+=ceil(num/banana)
            if(time<=k):
                high=banana-1
            else:
                low=banana+1
    return low
arr=[3,6,7,11]
k=8
print(kokoeatBanana(arr,k))'''
            
#Minimum days to make M bouquets
#using linear search
'''class Solution:
    def minDaysBloom(self, m, k, arr):
        # Code here
        if(m>len(arr)):
            return -1 
        Min=min(arr) 
        Max=max(arr) 
        for bloomday in range(Min,Max+1):
            count=0 
            noOfB=0 
            for flower in arr:
                if(flower<=bloomday):
                    count+=1 
                else:
                    noOfB+=count//k 
                    count=0 
            noOfB+=count//k 
            if(noOfB>=m):
                return bloomday 
        return -1 '''
#User function Template for python3

----------------------------------------------------------
'''class Solution:
    def minDaysBloom(self, m, k, arr):
        # Code here
        if(m>len(arr)):
            return -1 
        low=min(arr) 
        high=max(arr) 
        ans = -1 
        while(low<=high):
            bloomday=(low+high)//2 
            count=0 
            noOfB=0 
            for flower in arr:
                if(flower<=bloomday):
                    count+=1 
                else:
                    noOfB+=count//k 
                    count=0 
            noOfB+=count//k 
            if(noOfB<m):
                low=bloomday+1 
            else:
                ans=bloomday 
                high=bloomday-1 
        return ans'''
    
    
    
#using binary search
    