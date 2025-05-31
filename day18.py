'''print("hello")'''


#max consecutive ones 3(leet code)==optimal solution
#Time com:O(N)
'''def longestOnes(nums,k):
    n=len(nums)
    left=0
    right=0
    maxLen=0
    count_zeros=0
    while(right<n):
        if(nums[right]==0):
            count_zeros+=1
        if(count_zeros>k):
            while(count_zeros>k):
                if(nums[left]==0):
                    count_zeros-=1
                left+=1
        maxLen=max(maxLen,right-left+1)
        right+=1
    return maxLen
nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
print(longestOnes(nums,k))'''  #OUTPUT:6


#fuits into basket leetcode (Brute force)
#Time com:O(N**2)
'''def tatalfruits(fruits,k):
    n=len(fruits)
    maxLen=0
    for i in range(0,n):
        s=set()
        for j in range(i,n):
            s.add(fruits[j])
            if(len(s)>2):
                break
            maxLen=max(maxLen,j-i+1)
    return maxLen
fruits= [1,2,1]
k=2
print(tatalfruits(fruits,k))'''
   
   
   
#Optimal solution for fruits into basket
#Time com:O(N) 
'''def totalFruit(fruits,k):
    n=len(fruits)
    left=0
    right=0
    maxLen=0
    d={}
    while(right<n):
        if(fruits[right] in d):
            d[fruits[right]]+=1
        else:
            d[fruits[right]]=1
        if(len(d)>2):
            while(len(d)>2):
                d[fruits[left]]-=1
                if(d[fruits[left]]==0):
                    del d[fruits[left]]
                left+=1
        maxLen=max(maxLen,right-left+1)
        right+=1
    return maxLen
fruits= [1,2,1]

k=2
print(totalFruit(fruits,k))'''
   
   
   
def maxsubarray(nums):
    n=len(nums)
    maxsum=float("-inf")
    for i in range(0,n):
        for j in range(i,n):
            Sum=sum(nums[i:j+1])
            maxsum=max(maxsum,Sum)
    return maxsum
nums= [-2,1,-3,4,-1,2,1,-5,4]  
print(maxsubarray(nums))   