# to print the characters using ascii

#1..chr() method :it prints the character for the given ascii value
#chr(86)

#2..ord() method:it prints the ascii valur for the given character
#ord("A")

# space =32
# 0 = 48 to 9 = 57
# A = 65 to Z = 90
# a = 97 to z = 122
# @ = 64
# ! = 33
 
 
# to print all the ascii values
'''for i in range(128):
    print(i, "->", chr(i))'''


# enter a char and print ascii value 
'''n=input()
ascii=ord(n)
print("ascii:",ascii)'''

# eneter num and print ascii value
'''n=int(input())
ascii=chr(n)
print("ascii:",ascii)'''

# print lower case ascii values
'''for i in range(97,128):
    print(chr(i),":",i)'''
    
#print upper case ascii values
'''for i in range(67,90):
    print(chr(i),":",i)'''
