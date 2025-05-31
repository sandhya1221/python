#prime numbers
'''n=int(input())
for i in range(1,n+1):
    if(n%i==0):
        print(i)'''
        
#count primes
'''def isPrime(num):
    c=0
    for i in range(1,num+1):
        if(num%i==0):
            c+=1
    return c==2
n=int(input())
count=0
for num in range(2,n):
    if(isPrime(num)):
        count+=1
print("count of primes:",count)'''

#count primes (SIEVE OF EROTHENESES)
#t.c:O(n log log n)=O(1)
n=int(input())
prime=[1]*n
for i in range(2,int(n**0.5)+1):
    if(prime[i]==1):
        for j in range(i*i,n,i):
            prime[j]=0
count=0
for i in range(2,n):
    if(prime[i]==1):
        count+=1
print(count)

'''=================================================='''

#sort chracters by frequency(leetcode )


'''============================================================================'''


#search in 2D matrix(leetcode 74)
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
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
target=14
print(searchMatrix(matrix,target))'''


#Rotate matrix(leetcode ) t.c:O(N2) sc:O(n**2) 
#normal approach(method 1)
'''def rotate(matrix):
    n=len(matrix)
    m=len(matrix[0])
    dupMat=[]
    for i in range(n):
        temp=[0]*n
        dupMat.append(temp)
    for i in range(0,n):
        for j in range(0,n):
            dupMat[j][n-i-1]=matrix[i][j]
    for i in range(0,n):
        for j in range(0,n):
            matrix[i][j]=dupMat[i][j]
    print(matrix)
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))'''

#Easy approach(Rotate image)
#TC:  SC:O(1)
#optimal solution
'''def rotate(matrix):
    n=len(matrix)
    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i]=matrix[i][::-1]
    print(matrix)
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))'''

'''==================================================================================='''

#matrix diagonal sum
def matrixsum(matrix):
    n=len(matrix)
    Sum=0
    for i in range(n):
        Sum+=matrix[i][i]
        Sum+=matrix[i][n-1-i]
    if(n%2==1):
        Sum-=matrix[n//2][n//2]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrixsum(matrix))
        
      
                