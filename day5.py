#creating arr to dict
'''n=[1,1,2,3,2,1]
d={}
for i in n:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)'''


#two sum in leetcode using dictionary 
'''def twoSum(nums, target):
    d={}
    n=len(nums)
    for a in range(0,n):
        b=target-nums[a]
        if(b in d):
            return [a,d[b]]
        else:
            d[nums[a]]=a
nums=list(map(int,input().split()))
target=9
print(twoSum(nums,target))'''

#two sum using two pointers the array must be sorted
'''def twoSum(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while(low<high):
        sum=nums[low]+nums[high]
        if(sum==target):
            return "Yes"
        elif(sum>target):
            high-=1
        elif(sum<target):
            low+=1
    return "No"
nums=list(map(int,input().split()))
target=int(input())
print(twoSum(nums,target))'''

#3 sum using for loops
'''def threeSum(nums):
    triplet_sum=set()
    n=len(nums)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(nums[i]+nums[j]+nums[k]==0):
                    temp=[nums[i],nums[j],nums[k]]
                    temp.sort()
                    triplet_sum.add(tuple(temp))
                        
ans=[]
for triplet in triplet_sum:
    ans.append(list(triplet))
nums=int(input())
print(threeSum(nums))   ''' 

#3sum using hashing with 3 pointers
'''def threesum(nums):
    nums.sort()
    n=len(nums)
    ans=[]
    for i in range(0,n):
        if i>0 and nums[i]==nums[i-1]:
            continue
        j=i+1
        k=n-1
        while (j<k):
            Sum=nums[i]+nums[j]+nums[k]
            if(Sum<0):
                j+=1
            elif(Sum>0):
                k-=1
            else:
                temp=[nums[i],nums[j],nums[k]]
                ans.append(temp)
                j+=1
                k-=1
                while(j<k and nums[j-1]==nums[j]):
                    j+=1
                while(j<k and nums[k+1]==nums[k]):
                    k-=1
    return ans
nums=[-1,0,1,2,-1,-4]
print(threesum(nums))'''

#majority element 2
'''d={}
n=len(nums)
for i in nums:
    if(i in d):
        d[i]=d[i]+1
    else:
        d[i]=1
        for keys,values in d.items():
            if(values>n//3):'''
            
#functions
#def fun(): # it is defing a function
#calling function is not having def ,,,,when fun call comes then definiitley function definition should be executed
#calling fun: fun() without def
# in return if there is any stataments it will check that statments and prints and then goes to the next func call
#examples

'''def fun(x):
    if x==0:
        return
    print(x)
    fun(x-1)
fun(5)'''


#this is the example for print statements after the conditions which is there in after print statement
'''def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)
fun(5)
'''

#time complexity analysing
#space complexity:whenever we take list,set dict,tuple at that point tha space is O(n)
# whenever we take matrix it will become O(n**2)

#a=[1 2 3]
# subsequences [1][2][3][1 2][2 3][1 2 3][1 3] for the above array
#Take/not take
#example a=[123]=8 outcomes should come

#recurssion:functions calling by itself until it reaches the base condition
#in recursion always executes the left
             
             

       
                
                


        



   