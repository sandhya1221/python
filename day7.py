# SORTING ALGORITHM
#practice well this code

'''nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
i=0
j=0
result=[]
while(i<len(nums1) and j<len(nums2)):
    if(nums1[i]<=nums2[j]):
        result.append(nums1[i])
        i+=1
    else:
        result.append(nums2[j])
        j+=1
while(i<len(nums1)):
    result.append(nums1[i])
    i+=1
while(i<len(nums2)):
    result.append(nums2[j])
    j+=1
print(result)'''


#SBI(sorting bubble Insertion)
    
#MERGE SORT(codestudio) Time compl:O(n log n) space:O(n)
'''def mergeSort(arr,n):
    def mS(arr,low,high):
        if(low==high):
            return
        mid=(low+high)//2
        mS(arr,low,mid)
        mS(arr,mid+1,high)
        Sort(arr,low,mid,high)
    def Sort(arr,low,mid,high):
        i=low
        j=mid+1
        k=[]
        while(i<=mid and j<=high):
            if(arr[i]<=arr[j]):
                k.append(arr[i])
                i+=1
            else:
                k.append(arr[j])
                j+=1
        while(i<=mid):
            k.append(arr[i])
            i+=1
        while(j<=mid):
            k.append(arr[j])
            j+=1
        for ind,val in enumerate(k):
            arr[ind+low]=val
    low=0
    high=n-1
    mS(arr,low,high)
    return arr
arr=[1,5,4,3,2] 
n=len(arr)
print(mergeSort(arr,n))'''


#QUICK SORT(Time comp:O(n log n),space:O(1)
#it consumes less space
# it will take a pivot value
'''def quickSort(arr):
    def qs(arr,low,high):
        if(low<high):
            pIndex=partition(arr,low,high)
            qs(arr,low,pIndex-1)
            qs(arr,pIndex+1,high)
    def partition(arr,low,high):
        i=low
        j=high
        pivot=arr[low]
        while(i<j):
            while(arr[i]<=pivot and i<high):
                i+=1
            while(arr[j]>=pivot and j>low):
                j-=1
            if(i<j):
                arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j
    n=len(arr)
    low=0
    high=n-1
    qs(arr,low,high)
    return arr
arr=[4,6,3,9,8,2,1]
print(quickSort(arr))'''



#using functions swapping
'''def swap(a,b):
    a[0],b[0]=a[0],b[0]
a=5
b=8'''

#SBI(selection,Bubble,Insertion)
#1.SELECTION:it will select the min elements and swap with the perfect positions)(small to big)
'''def Selection(arr):
    n=len(arr)
    for i in range(0,n):
        Min=i
        for j in range(i+1,n):
            if(arr[j]<arr[Min]):
                Min=j
        arr[i],arr[Min]=arr[Min],arr[i]
    return arr
arr=[13,46,24,52,20,9]
n=len(arr)
print(Selection(arr))'''


#2.BUBBLE SORT(largest to small)
#if you dont the code u type as arr.sort() and return arr

'''def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[5,4,13,56,78]
print(bubbleSort(arr))'''

#INSERTION SORT:compares an element with its left adjacent element,if it is lesser dont swap.otherwise swaps
# Time comp:O(n**2) space comp:O(1)
'''
def insertion(arr):
    n=len(arr)
    for i in range(0,n):
        while(i>0 and arr[i-1]>arr[i]):
            arr[i-1],arr[i]=arr[i],arr[i-1]
            i-=1
    return arr
arr=[14,9,15,12,6,8,13]
print(insertion(arr))''' 

#WORD REVERSE
'''s="hey hii hello"
s=s.split(" ")
s=s[::-1]'''
#print(*s) #converting from list to string
#print(" ".join(s))
#print("you ".join(s))

#anagram code leetcode 
'''def word(s,t):
    return sorted(s)==sorted(t)
s="anagram"
t="nagaram"
print(word(s,t))'''

#TOWER OF HANOI
def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disc 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, destination, helper)
    print(f"Move disc {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, helper, source, destination)

# Call for 3 discs
tower_of_hanoi(3, 'A', 'B', 'C')




        
        
            
        