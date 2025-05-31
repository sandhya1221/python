# spiral Order (leetcode 54)
'''def spiralOrder(matrix):
    n=len(matrix)
    m=len(matrix[0])
    sr=0
    er=n-1
    sc=0
    ec=m-1
    result=[]
    while(sr<=er and sc<=ec):
        for i in range(sc,ec+1):
            result.append(matrix[sr][i])
        sr+=1
        for i in range(sr,er+1):
            result.append(matrix[i][ec])
        ec-=1
        if(sr<=er):# to check whether  we have other row or not
            for i in range(ec,sc-1,-1):
                result.append(matrix[er][i])
            er-=1
        if(sc<=ec):
                #Bottoam to top
            for i in range(er,sr-1,-1):
                result.append(matrix[i][sc])
            sc+=1
    return result
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiralOrder(matrix))'''


#u ar given a string S,consisting of lowercase english letter u can apply this operation to the string S exactly once.
# choose any index i and move the character S[i] to the beginning of the string(deleting it from the th original position fnd the lexicographically minimal string that can be obtained after perfoming operation)
#input format:the input consists of a single line the line contains the sting S


#Agressive cows(Binary search)chatgpt
'''def aggressiveCows( stalls, k):
    def canWePlace(minDist, stalls, k):
        cow = stalls[0]
        placedCows = 1
        for i in range(1, len(stalls)):
            if stalls[i] - cow >= minDist:
                cow = stalls[i]
                placedCows += 1
            if placedCows >= k:
                return True
        return False

    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if canWePlace(mid, stalls, k):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans
stalls=[10,1,2,7,5]
k=3
print(aggressiveCows(stalls,k))'''

#aggresive cows
def aggressiveCows(stalls,k):
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
    for minDist in range(1,Max-Min+1):
        if(canWePlace(minDist,stalls,k)):
            continue
        else:
            return minDist-1
stalls=[10,1,2,7,5]
k=3
print(aggressiveCows(stalls,k))
        
    

                