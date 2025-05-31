# power of 2 leetcode 50 
'''def pow(x,n):
    if(n<0):
        x=1/x
    n=abs(n) # conevert negative to positive
    ans=1
    for i in range(n):
        ans=ans*x
    return ans
x=2
n=3
print(pow(x,n))'''

#power of two in simple
'''x=2
n=3
print(x**n)'''

#check leetcode 78 SUBSET PROBLEM
def generate(ind,curr,ans,nums):
    if ind==len(nums):
        ans.append(curr.copy())
        return
    curr.append(nums[ind])
    generate(ind+1,curr,ans,nums)
    curr.pop()
    generate(ind+1,curr,ans,nums)
def subset(nums):
    ans=[]
    generate(0,[],ans,nums)
    return ans
nums=[1,2,3]
print(subset(nums)) # OUTPUT:[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

#check the subsets
'''def generate(self,ind,curr,ans,nums):
    if(ind==len(nums)):
        ans.append(curr.copy())
        return
        curr.append(nums[ind])
        self.generate(ind+1,curr,ans,nums)
        curr.pop()
        self.generate(ind+1,curr,ans,nums)
def subsets(self, nums,curr,ans):
    ind=0
    curr=[]        
    ans=[]
    self.generate(ind,curr,ans,nums)

nums=[1,2,3]
print(generate(ind,curr,ans,nums))'''

#Check if there exists a subsequence with sum K(geeks for geeks)



# COMBINATION SUM2 (leetcode)

'''def generate(ind,curr,ans,candidates,target):   #see this code in leetcode 39
    if(target==0):
        ans.append(curr.copy())
        return
    if(target<0):
        return
    if(ind==len(candidates)):
        return
    curr.append(candidates[ind])
    generate(ind,curr,ans,candidates,target-candidates[ind])
    curr.pop()
    generate(ind+1,curr,ans,candidates,target)
def combinationSum2(candidates,target):
    candidates.sort()
    ans=[]
    generate(0,[],ans,candidates,target)
    return ans
candidates=[2,3,6,7]
target=7
print(combinationSum2(candidates,target))
OUTPUT:[[2,2,3]],[7]]'''


# leetcode 2828 Acronym question 
'''def acronym(words,s):
    acronym=''
    for word in words:
        acronym+=word[0]
    return acronym==s
words=["apple","banana"]
s="ab"
print(acronym(words,s))'''

#check acronym with case insensitivity for example if i give apple like this lower case but also im printing as Apple it should give true
'''def acronym(words,s):
    acronym=''
    for word in words:
        acronym+=word[0].lower()
    return acronym==s.lower()
words=["Apple","Banana"]
s="ab"
print(acronym(words,s))'''



#longest common prefix
''''def commonprefix(arr):
    if not arr:
        return""
    first=arr[0]
    last=arr[-1]
    i=0
    while i<len(first) and i<len(last) and first[i]==last[i]:
        i+=1
    return first[:i]
arr=["flower","flight","flue"]
print(commonprefix(arr))'''
    
    
    
       
    
