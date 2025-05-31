# missing positive values in array
# input=[1,2,3,4] len=5 output=5
# input=[1,4,2] len=4 output=3
'''n=[1,2,3,4]
missing=sum(range(1,len(n)+2))-sum(n)
print(missing)'''



# zero in last
'''arr=[0,1,0,3,12]
res=[]
for x in arr:
    if x!=0:
        res.append(x)
zeros=arr.count(0)
res+=[0]*zeros
print("after moving zeros:",res)'''



'''a=[1,2,3,0,4,2]
for i in a:
    if i==0:
        a.remove(0)
        a.append(0)
print(a) '''

# even in last = [2, 3, 4, 5, 7]
'''n=[2,3,4,5,7]
res = []
for i in n:
    if i % 2 != 0:
        res.append(i)
for k in n:
    if k % 2 == 0:
        res.append(k)
print("After moving even:", res)'''

#two pointer
'''n=[1,3,5,2,4]
k=0
for i in range(len(n)):
    if n[i]%2!=0:
        n[k],n[i]=n[i],n[k]
        k+=1
print(n)
'''

