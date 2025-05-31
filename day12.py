#Aggressive cows(Binaray search)
'''def agressiveCows(stalls,k):
    def canWePlace(minDist,stalls,k):
        cow=stalls[0]
        placedCows=1
        for stall in range(1,len(stalls)):
            if(stalls[stall]-cow>=minDist):
                cow=stalls[stall]
                placedCows+=1
            if(placedCows==k):
                return True
        return False
    stalls.sort()
    Min=min(stalls)
    Max=max(stalls)
    if(k==2):
        return Max-Min
    low=1
    high=max(stalls)
    while(low<=high):
        minDist=(low+high)//2
        if(canWePlace(minDist,stalls,k)):
            low=minDist+1
        else:
            high=minDist-1
    return high

stalls=[10,1,2,7,5]
k=3
print(agressiveCows(stalls,k))'''

# Allocate Minimum pages  (High Time complexity)
'''def findPages(arr,k):
    def canWeAllocate(maxPages,arr):
        no_of_pages_allocated=arr[0]
        students=1
        for pages in range(1,len(arr)):
            if(arr[pages]+no_of_pages_allocated<=maxPages):
                no_of_pages_allocated+=arr[pages]
            else:
                no_of_pages_allocated=arr[pages]
                students+=1
        return students
    if(k>len(arr)):
        return -1
    Min=max(arr)
    Max=sum(arr)
    for maxPages in range(Min,Max+1):
        if(canWeAllocate(maxPages,arr)<=k):
            return maxPages
arr=[12, 34, 67, 90] 
k = 2
print(findPages(arr,k))'''

#Binary search
'''def findPages(arr,k):
    def canWeAllocate(maxPages,arr):
        no_of_pages_allocated=arr[0]
        students=1
        for pages in range(1,len(arr)):
            if(arr[pages]+no_of_pages_allocated<=maxPages):
                no_of_pages_allocated+=arr[pages]
            else:
                no_of_pages_allocated=arr[pages]
                students+=1
        return students
    if(k>len(arr)):
        return -1
    low=max(arr)
    high=sum(arr)
    while(low<=high):
        maxPages=(low+high)//2
        if(canWeAllocate(maxPages,arr)<=k):
            high=maxPages-1
        else:
            low=maxPages+1
    return low
arr=[12, 34, 67, 90] 
k = 2
print(findPages(arr,k))
'''
        
#similar solution for painters partition problem(max(min))
'''Geeks for geeks'''

#similar solution for split array into k parts problem(max(min))
'''geeks for geeks'''


#STACK
#LIFO
'''print(dir(list))'''

'''stack=[]
print(type(stack))'''

'''stack=[]
stack.append(10)
print(stack)'''


'''stack=[]
stack.append(10)
print(stack)
stack.append(20)
print(stack)'''


'''stack=[]
stack.append(10)
print(stack)
stack.append(20)
print(stack)
print(stack[-1])'''

#Valid parentheses(normal solution)
'''def validParentheses(s):
    stack=[]
    for ele in s:
        if(ele in "([{"):
            stack.append(ele)
        else:
            if(len(stack)==0):
                return False
            x=stack.pop()
            if(x=="(" and ele==")" or x=="[" and ele=="]" or x=="{" and ele=="}"):
                continue
            else:
                return False
    return len(stack)==0
s="()"
print(validParentheses(s))'''
            

# Trapping rain water
def trap(height):
    n=len(height)
    leftMax=[-1]*n
    leftMax[0]=height[0]
    for i in range(1,n):
        leftMax[i]=max(height[i],leftMax[i-1])
        rightMax=[-1]*n
        rightMax[n-1]=height[n-1]
    for i in range(n-2,-1,-1):
        rightMax[i]=max(height[i],rightMax[i+1])
        MinArray=[]
    for i in range(0,n):
        MinArray.append(min(rightMax[i],leftMax[i]))
    result=0
    for i in range(0,n):
        result+=MinArray[i]-height[i]
    return result 
height=[4,2,0,3,2,5]
print(trap(height))