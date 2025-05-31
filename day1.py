        
#conerting lower letter to upper case and vice versa
'''s = "AbcdEFGH"
for ch in s:
    if 'a'<=ch<='z':
        print(chr(ord(ch)-32),end="")  
    else:
        print(chr(ord(ch)+32),end="")
'''


#print('a'<'b')

'''
s1="abcd"
s2="jk"
i=0
res=""
while  i<len(s1) and i<len(s2):
    res+=(s1[i]+s2[i])
    i+=1
while i<len(s1):
    res+=chr(ord(s1[i])-32)
    i+=1
while i<len(s2):
    res+=chr(ord(s2[i])-32)
    i+=1
print(res)'''



# given string is present in the original string or not
'''s1="abcd"
s2="f"
for i in s2:
    if s2 in s1:
        print("True")
        break
    else:
        print("False")
    
        '''
#circular 
'''s1="abcde"
s2="dea"
doubled=s1+s1
print(doubled)
if s2 in doubled:
    print("True")
else:
    print("False")'''
    
#3a4d5c
'''s="3a4d5c"
output=""
for i in range(0,len(s),2):
    count=int(s[i])
    char=s[i+1]
    output+=char*count
print(output)'''


 #31a4b11c
str="31a4b11c"
res=""
num=""
for i in str:
    if i.isdigit():
        num+=i
    else:
        res+=int(num)*i
        num=""
print(res)

#13b12aa
