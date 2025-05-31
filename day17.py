#subarray generation
'''arr=list(map(int,input().split()))
n=len(arr)
for i in range(0,n):
    for j in range(i,n):
        print(arr[i:j+1])'''  #OUTPUT  5 10 8
'''[5]
[5, 10]
[5, 10, 8]
[10]
[10, 8]
[8]'''
        
        
'''================================================================================================'''

#Control window  Time Com:O(N**2)    
'''arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
maxSum=0
for i in range(0,n):
    for j in range(i,n):
        if(len(arr[i:j+1])==k):
            maxSum=max(maxSum,sum(arr[i:j+1]))
print(maxSum)'''

#optimal solution sh:sub move  ex:move add
'''arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
left=0
right=k-1
Sum=sum(arr[left:right+1])
maxSum=Sum
while(right<n-1):
    Sum-=arr[left]
    left+=1
    right+=1
    Sum+=arr[right]
    maxSum=max(maxSum,Sum)
print(maxSum)'''


'''==============================================================================================='''


#find the longest or the smallest element with conditions using Brute force algorithm
#time com is high
'''arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
maxLen=0
for i in range(0,n):
    for j in range(i,n):
        if(sum(arr[i:j+1])<k):
            maxLen=max(maxLen,j-i+1)
print(maxLen)'''


#optimal solution
#Time com:O(2N)
'''arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
maxLen=0
left=0
right=0
Sum=0
while(right<n):  #out of bound
    Sum+=arr[right]  #expand
    while(Sum>k):
        Sum-=arr[left] #shrink
        left+=1
    maxLen=max(maxLen,right-left+1)
    right+=1
print(maxLen)'''

#more optimal solution
#shrinking one-one-one time
#Time com=O(N)
arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
maxLen=0
left=0
right=0
Sum=0
while(right<n): #O(N)
    Sum+=arr[right]
    if(Sum>k):
        Sum-=arr[left]
        left+=1
    maxLen=max(maxLen,right-left+1)
    right+=1
print(maxLen)