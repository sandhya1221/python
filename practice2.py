'''def searchMatrix(matrix,target):
    n=len(matrix)
    m=len(matrix[0])
    row=0
    col=m-1
    while(row<n and col>=0):
        if(matrix[row][col]==target):
            return True
        elif(target>matrix[row][col]):
            row+=1
        elif(target<matrix[row][col]):
            col-=1
    return False
matrix=[[1,2,3],[4,5,6],[7,8,9]]
target=7
print(searchMatrix(matrix,target))'''


#Linear search
'''def linear(arr,target):
    n=len(arr)
    for index in range(n):
        if arr[index]==target:
            return index
    return -1
arr=[2,4,5,3,8]
target=5
print(linear(arr,target))'''

'''a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
    print("largest element is:",a) 
if(b>a and b>c):
    print("largest element is:",b) 
elif(c>a and c>b):
    print("largest element is:",c) '''
    
'''arr=list(map(int,input().split()))
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print("largest element:",i)'''

'''arr=list(map(int,input().split()))
n=len(arr)

largest=sec_largest=float('-inf')
for i in range(0,len(arr)):
    if arr[i]>largest:
        sec_largest=largest
        largest=arr[i]
print("largest:",sec_largest)'''

'''def sum_ele(arr,n):
    n=len(arr)
    sum=0
    for i in range(0,n):
        sum+=arr[i]
    return sum
n=3
arr=[1,2,3]
print(sum_ele(arr,n))'''

# to sort or not
'''def sort(arr):
    arr.sort()
    return True
n=5
arr=[2,3,1,4,9]
print(sort(arr))
print(arr)'''




#check whether arr is sorted or not
'''def is_sort(arr):
    return arr==sorted(arr)
arr=[2,3,1,4,9]
print(is_sort(arr))'''

#sum
'''def sums(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum
arr=[2,3,4]
print(sums(arr))
'''
    
'''def evod(arr):
    even_count=0
    odd_count=0
    for n in arr:
        if n%2==0:
            even_count+=1
        else:
            odd_count+=1
    return even_count,odd_count

n=[1,2,3,4,5,6]  
even,odd=evod(n)
print("even numbers:",even)
print("odd numbers:",odd)'''


'''list=[10,20,30]
sum=0
for i in list:
    sum+=i
print(sum)'''


'''s=[15,2,7,25]
max=s[0]
min=s[0]
for i in s:
    if i>max:
        max=i
    if i<min:
        min=i
print("max num",max)
print("min num",min)'''

'''a=[10,20,10,30]
a.sort()
a=list(set(a))
print(a)'''

a=[10,20,10,30]
unique=[]
for i in a:
    if i not in unique:
        a.append(unique)
print(unique)


'''=[10,20,10,30]
ans=[]
count=0
for i in a:
    if i not in ans:
        a.append(i)
        count+=1
print(count)
'''