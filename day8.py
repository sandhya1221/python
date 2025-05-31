#Binary search sample program
'''def binarySearch(arr,k):
    n=len(arr)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==k):
            return mid
        elif(k>arr[mid]):
            low=mid+1
        elif(k<arr[mid]):
            high=mid-1
    return -1
arr=[1,2,3,7,5,6]
k=5
print(binarySearch(arr,k))'''


#LOWER BOUND (binary search)
def lowerbound(arr,target):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>=target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[1,3,5,6,8,9,15]
target=9
print(lowerbound(arr,target))
    
    
#UPPER BOUND
'''def upperbound(arr,target):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[1,3,5,6,8,9,15]
target=9
print(upperbound(arr,target))'''

#Search insert position of K in a sorted array
# using lower bound
'''def SearchInsert(arr,k):
    n=len(arr)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>k):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=[1,3,5,6,8,9,15]
k=9
print(SearchInsert(arr,k))'''

#floor and ceil position gfg

#floor:larget element in the array such that arr[ind]<=x
#ceil:samllest elemnt in the array such that arr[ind]>=x (lower bound)
'''def getFloorAndCeil(x,arr):
    def getFloor(x,arr):
        n=len(arr)
        low=0
        high=n-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]<=x):
                ans=arr[mid]
                low=mid+1
            else:
                high=mid-1
        return ans
    def getCeil(x,arr):
        n=len(arr)
        low=0
        high=n-1
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            if(arr[mid]>=x):
                mid=ans
            else:
                high=mid+1
        return ans
    floor = getFloor(x, arr)
    ceil = getCeil(x, arr)
    print(f"Floor: {floor}, Ceil: {ceil}")'''

#search in rotated sorted ( leetcode 33)
'''def search(arr,key):
    n=len(arr)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==key):
            return mid
        elif(arr[low]<=arr[mid]):
            if(arr[low]<=key<=arr[mid]):
                high=mid-1
            else:
                low=mid+1
        elif(arr[mid]<=arr[high]):
            if(arr[mid]<=key<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return -1
arr=[3,5,1,2]
key=8
print(search(arr,key))'''

#MeTHOD 2 (search in rotated sorted array) done in gfg

#find sorted and rotated min(gfg)
'''def findMin(arr):
    n=len(arr)
    low=0
    high=n-1
    Min=float("inf")
    while(low<=high):
        mid=(low+high)//2
        if(arr[low]<=arr[mid]):
            if(arr[low]<Min):
                Min=arr[low]
            low=mid+1
        if(arr[mid]<=arr[high]):
            if(arr[mid]<Min):
                Min=arr[mid]
            high=mid-1
    return Min
arr=[5,6,1,2,3,4]
print(findMin(arr))'''

#finf kth rotations in gfg
'''def findKRotation(arr):
    n=len(arr)
    low=0
    high=n-1
    Min=float("inf")
    mIndex=0
    while(low<=high):
        mid=(low+high)//2
        if(arr[low]<=arr[mid]):
            if(arr[low]<Min):
                Min=arr[low]
                mIndex=low
            low=mid+1
        elif(arr[mid]<=arr[high]):
            if(arr[mid]<Min):
                Min=arr[mid]
                mIndex=mid
            high=mid-1
    return mIndex
arr=[5,6,1,2,3,4] 
print(findKRotation(arr))'''
                
            

    